
import models.ResNet as resnet

print("running image analyzer")

dualnet = resnet.resnet50(pretrained=True)

print("end image analyzer")
