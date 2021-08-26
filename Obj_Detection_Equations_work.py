from detect import run

# Local
Local_video = "data/images/Road_Traffic2_short.mp4"

# Indonesia, 	Bekasi.
Indonesia_Bekasi = "http://209.143.54.211:80/mjpg/video.mjpg"

# Netherlands, Zeeland
Netherlands_Zeeland =  "http://217.63.79.153:8081/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER"

# Germany, 	Essen.
Germany_Essen = "http://178.203.165.119:8082/mjpg/video.mjpg"

# United States, Jackson stream Youtube Stream
United_States_Jackson = "https://youtu.be/FmoclK_hKz8"

# Karnataka, Banglore
Karnataka_Banglore = "http://117.192.41.101:81/jpgmulreq/1/image.jpg?key=1516975535684&lq=1&COUNTER"

# Spain,Barcelona
Spain_Barcelona = "http://210.136.243.194:82/cgi-bin/camera?resolution=640&amp;quality=1&amp;Language=0&amp;1629968232"

#	Switzerland, 	Basel.
Switzerland_Basel = "http://31.164.218.109:50001/axis-cgi/mjpg/video.cgi?camera=&resolution=640x480"
# Source = Indonesia_Bekasi
i = 0
def Run_Obj_Detect(Source):
        frames = run(weights='yolov5s.pt',  # model.pt path(s)
                source=Source,  # file/dir/URL/glob, 0 for webcam
                imgsz=640,  # inference size (pixels)
                conf_thres=0.25,  # confidence threshold
                iou_thres=0.45,  # NMS IOU threshold
                max_det=1000,  # maximum detections per image
                device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
                view_img=False,  # show results
                save_txt=False,  # save results to *.txt
                save_conf=False,  # save confidences in --save-txt labels
                save_crop=False,  # save cropped prediction boxes
                nosave=False,  # do not save images/videos
                classes=None,  # filter by class: --class 0, or --class 0 2 3
                agnostic_nms=False,  # class-agnostic NMS
                augment=False,  # augmented inference
                visualize=False,  # visualize features
                update=False,  # update all models
                project='static/OutPut',  # save results to project/name
                name='',  # save results to project/name
                exist_ok=True,  # existing project/name ok, do not increment
                line_thickness=3,  # bounding box thickness (pixels)
                hide_labels=False,  # hide labels
                hide_conf=False,  # hide confidences
                half=False,  # use FP16 half-precision inference
                )

        return frames