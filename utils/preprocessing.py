from torchvision import transforms

transform_resnet = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def preprocess_resnet(image):
    image = transform_resnet(image)
    image = image.unsqueeze(0)
    return image

transform_efficientnet = transforms.Compose([
    transforms.Resize(320),
    transforms.CenterCrop(300),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def preprocess_efficientnet(image):
    image = transform_efficientnet(image)
    image = image.unsqueeze(0)
    return image