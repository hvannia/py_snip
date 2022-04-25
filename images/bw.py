from PIL import Image

image = "ivan_hugo_200701.JPG"

color_image = Image.open(f"images/{image}")
gray_scale = color_image.convert("L")
gray_scale.save(f"images/gray_{image}")
