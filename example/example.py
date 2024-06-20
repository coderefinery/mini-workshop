from noise import add_noise
from filters import gaussian_smoothing, denoise, warhol_effect, grayscale, pixelate
from file_io import read_image, save_image
from metrics import mean_squared_error


image = read_image("data/astronaut.jpg")
print(image.shape)


image_grayscale = grayscale(image)
save_image(image_grayscale, "generated/astronaut-grayscale.jpg")


image_noisy = add_noise(image, amount=0.15)
save_image(image_noisy, "generated/astronaut-noisy.jpg")
print(mean_squared_error(image, image_noisy))


image_smoothed = gaussian_smoothing(image_noisy, sigma=5)
save_image(image_smoothed, "generated/astronaut-smoothed.jpg")
print(mean_squared_error(image, image_smoothed))


image_denoised = denoise(image_noisy, magic_factor=1.2)
save_image(image_denoised, "generated/astronaut-denoised.jpg")
print(mean_squared_error(image, image_denoised))


image_effect = warhol_effect(image)
save_image(image_effect, "generated/astronaut-warhol.jpg")


image_pixelated = pixelate(image, scale=0.05, num_colors=8)
save_image(image_pixelated, "generated/astronaut-pixelated.jpg")


image_reference = read_image("reference/astronaut-pixelated.jpg")
print(mean_squared_error(image_pixelated, image_reference))
