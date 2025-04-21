from PIL import Image

# 원본 이미지 열기
image = Image.open("sample.jpg")

# 흑백(그레이스케일)으로 변환
gray_image = image.convert("L")

# 변환된 이미지 저장
gray_image.save("sample_gray.jpg")

# 저장된 흑백 이미지 보기
gray_image.show()

print("이미지를 흑백으로 변환하여 저장하고 띄웠습니다!")

