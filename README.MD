# Puts watermark on images using relative or absolute coordinates. 

```python

from cv2watermark import (
    merge_image_percentage_height,
    merge_image_percentage_width,
    merge_image_percentage_height_position,
    merge_image_percentage_width_position,
    merge_image,
)

# Allowed image formats: url/path/buffer/base64/PIL/np
i2 = r"https://www.python.org/static/img/psf-logo.png"  # Transparent image from URL doesn't work! You have to download it before
i2 = r"F:\neuedownloads\psf-logo.png"
i1 = r"https://github.com/hansalemaos/screenshots/raw/main/splitted1.png"  

merg1 = merge_image(
    back=i1, front=i2, x=10, y=30, save_path="f:\\cv2mergepics\\merg1.png"
)

```

<img src="https://github.com/hansalemaos/screenshots/raw/main/merg1.png"/>


```python


merg2 = merge_image_percentage_width(
    back=i1,
    front=i2,
    x=10,
    y=30,
    front_percentage_width=80,
    save_path="f:\\cv2mergepics\\merg2.png",
)


```

<img src="https://github.com/hansalemaos/screenshots/raw/main/merg2.png"/>


```python


merg3 = merge_image_percentage_width_position(
    back=i1,
    front=i2,
    percentx=50,
    percenty=60,
    front_percentage_width=30,
    save_path="f:\\cv2mergepics\\merg3.png",
)

```

<img src="https://github.com/hansalemaos/screenshots/raw/main/merg3.png"/>


```python



merg4 = merge_image_percentage_width(
    back=i1,
    front=i2,
    x=110,
    y=10,
    front_percentage_width=60,
    save_path="f:\\cv2mergepics\\merg4.png",
)

```

<img src="https://github.com/hansalemaos/screenshots/raw/main/merg4.png"/>


```python


merg5 = merge_image_percentage_width_position(
    back=i1,
    front=i2,
    percentx=50,
    percenty=10,
    front_percentage_width=40,
    save_path="f:\\cv2mergepics\\merg5.png",
)

```

<img src="https://github.com/hansalemaos/screenshots/raw/main/merg5.png"/>


```python


merg6 = merge_image_percentage_height(
    back=i1,
    front=i2,
    x=20,
    y=50,
    front_percentage_height=40,
    save_path="f:\\cv2mergepics\\merg6.png",
)


```

<img src="https://github.com/hansalemaos/screenshots/raw/main/merg6.png"/>


```python
merg7 = merge_image_percentage_height_position(
    back=i1,
    front=i2,
    percentx=20,
    percenty=40,
    front_percentage_height=40,
    save_path="f:\\cv2mergepics\\merg7.png",
)



```

<img src="https://github.com/hansalemaos/screenshots/raw/main/merg7.png"/>

