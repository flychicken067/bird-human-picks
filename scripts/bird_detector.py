"""COCO bird presence/count checks. These are triage signals, never species ID."""
import hashlib,json
from pathlib import Path
import numpy as np
from PIL import Image
import onnxruntime as ort

ROOT=Path(__file__).resolve().parents[1]
class BirdDetector:
 def __init__(self,variant='nano'):
  opt=ort.SessionOptions();opt.intra_op_num_threads=2;opt.log_severity_level=3
  prefix='yolov10s' if variant=='small' else 'yolov10n'
  self.variant=variant;p=ROOT/'models'/(prefix+'-onnx-model.onnx')
  provenance=p.parent/('detector-small-provenance.json' if variant=='small' else 'detector-provenance.json')
  self.provenance=json.loads(provenance.read_text());assert hashlib.sha256(p.read_bytes()).hexdigest()==self.provenance['sha256']
  self.session=ort.InferenceSession(str(p),sess_options=opt,providers=['CPUExecutionProvider'])
  self.input=self.session.get_inputs()[0].name
  assert json.loads((p.parent/(prefix+'-config.json')).read_text())['id2label']['14']=='bird'
 def detect(self,image):
  image=image.convert('RGB');w,h=image.size;scale=640/max(w,h);nw,nh=round(w*scale),round(h*scale)
  small=image.resize((nw,nh),Image.Resampling.BILINEAR)
  # Matches the model's fixed 640 top-left padding processor (not centered YOLO letterbox).
  canvas=Image.new('RGB',(640,640));canvas.paste(small,(0,0))
  inp=np.asarray(canvas,dtype=np.float32).transpose(2,0,1)[None]/255
  rows=self.session.run(None,{self.input:inp})[0].reshape(-1,6)
  boxes=[]
  for x1,y1,x2,y2,score,label in rows:
   if int(label)!=14 or score<.25:continue
   box=[max(0,float(x1)*w/nw),max(0,float(y1)*h/nh),min(w,float(x2)*w/nw),min(h,float(y2)*h/nh)]
   if box[2]<=box[0] or box[3]<=box[1]:continue
   boxes.append({'box':[round(x,2) for x in box],'score':round(float(score),5)})
  return boxes
 def assess(self,image):
  boxes=self.detect(image);strong=[b for b in boxes if b['score']>=.5]
  flags=[]
  if len(strong)==0:flags.append('no_confident_bird_detection')
  if len(boxes)>1:flags.append('multiple_birds_detected')
  if len(strong)==1:
   x1,y1,x2,y2=strong[0]['box'];w,h=image.size
   if max(x2-x1,y2-y1)<850:flags.append('detected_bird_below_850px')
   if x1<2 or y1<2 or x2>w-2 or y2>h-2:flags.append('detected_bird_touches_source_edge')
  return {'detections':boxes,'flags':flags,'species_identification':False,'expert_review':False,'detector_variant':self.variant,'detector_model':self.provenance['model'],'detector_revision':self.provenance['revision'],'detector_sha256':self.provenance['sha256']}

