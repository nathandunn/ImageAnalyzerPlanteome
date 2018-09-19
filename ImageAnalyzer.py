
import models.ResNet as resnet

print("running image analyzer")

dualnet = resnet.resnet50(pretrained=False)

print("end image analyzer")
