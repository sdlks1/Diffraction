from vpython import *
from raycast import *
from event import *


# Render
scene = canvas(width=1024, height=768, center=vec(0,0,0), background=vec(.6,.8,.8), range=15, fov=.001)
IMAGE_RES = .01
renderer = Renderer(IMAGE_RES)

# UI
wt_status = Label("Simulation Complete")
scene.append_to_caption("\n\n")

wt_slitN = Label("Slit Count")
slider_slitN = Slider(min=2, max=10, step=1, length=220, bind=event.push_N)
wt_slitN_v = Label(f"{slider_slitN.value()}")
scene.append_to_caption('\n')

wt_slitL = Label("Slit Spacing")
slider_slitL = Slider(min=1, max=1000, step=1, length=220, bind=event.push_L)
scene.append_to_caption('\t')
input_slitL = winput(bind=event.push_L_input)
wt_slitL_v = Label("倍波長")
scene.append_to_caption('\n')

wt_lambda = Label("Lambda")
slider_lambda = Slider(min=380, max=780, step=1, length=220, bind=event.push_Lambda)
wt_lambda_v = Label(f"{slider_lambda.value()} (nm)")
scene.append_to_caption('\n')

wt_distance = Label("Distance")
slider_distance = Slider(min=1, max=1000, step=1, length=220, bind=event.push_D)
scene.append_to_caption('\t')
input_distance = winput(bind=event.push_D_input)
# input_distance = winput(bind=db)
wt_distance_v = Label("倍波長")
scene.append_to_caption('\n\n')

btn_simulate = button(text="Simulate", bind=event.push_Sim)
scene.append_to_caption("\n\n\n")

wt_events = Label(f"{event.buffer}")



if __name__ == "__main__":
    print(type(vec(0,0,0)))