import torchvision.models as models

def vgg19():
    model = models.vgg19_bn(pretrained=False)
    return model
