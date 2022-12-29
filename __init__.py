import cv2
from a_cv_imwrite_imread_plus import open_image_in_cv, save_cv_image
from a_cv2_easy_resize import add_easy_resize_to_cv2

add_easy_resize_to_cv2()


def merge_image(back, front, x, y, save_path=None):
    back, front = _get_bf(back, front)
    meg = _merge_im(back, front, x, y)
    if save_path is not None:
        save_cv_image(save_path, meg)
    return meg


def _merge_im(back, front, x, y):
    bh, bw = back.shape[:2]
    fh, fw = front.shape[:2]
    x1, x2 = max(x, 0), min(x + fw, bw)
    y1, y2 = max(y, 0), min(y + fh, bh)
    front_cropped = front[y1 - y : y2 - y, x1 - x : x2 - x]
    back_cropped = back[y1:y2, x1:x2]

    alpha_front = front_cropped[:, :, 3:4] / 255
    alpha_back = back_cropped[:, :, 3:4] / 255
    result = back.copy()
    result[y1:y2, x1:x2, :3] = (
        alpha_front * front_cropped[:, :, :3]
        + (1 - alpha_front) * back_cropped[:, :, :3]
    )
    result[y1:y2, x1:x2, 3:4] = (
        (alpha_front + alpha_back) / (1 + alpha_front * alpha_back) * 255
    )
    return result


def _get_bf(back, front):
    back = open_image_in_cv(back, channels_in_output=4)
    front = open_image_in_cv(front, channels_in_output=4)
    return back, front


def merge_image_percentage_width(
    back,
    front,
    x,
    y,
    front_percentage_width,
    save_path=None,
    interpolation=cv2.INTER_AREA,
):
    back, front = _get_bf(back, front)
    front = cv2.easy_resize_image(
        front,
        width=int(back.shape[1] / 100 * front_percentage_width),
        height=None,
        percent=None,
        interpolation=interpolation,
    )
    meg = _merge_im(back, front, x, y)
    if save_path is not None:
        save_cv_image(save_path, meg)
    return meg


def merge_image_percentage_width_position(
    back,
    front,
    percentx,
    percenty,
    front_percentage_width,
    save_path=None,
    interpolation=cv2.INTER_AREA,
):
    back, front = _get_bf(back, front)
    front = cv2.easy_resize_image(
        front,
        width=int(back.shape[1] / 100 * front_percentage_width),
        height=None,
        percent=None,
        interpolation=interpolation,
    )
    x = int(back.shape[1] / 100 * percentx)
    y = int(back.shape[0] / 100 * percenty)
    meg = _merge_im(back, front, x, y)
    if save_path is not None:
        save_cv_image(save_path, meg)
    return meg


def merge_image_percentage_height(
    back,
    front,
    x,
    y,
    front_percentage_height,
    save_path=None,
    interpolation=cv2.INTER_AREA,
):
    back, front = _get_bf(back, front)
    front = cv2.easy_resize_image(
        front,
        width=None,
        height=int(back.shape[1] / 100 * front_percentage_height),
        percent=None,
        interpolation=interpolation,
    )
    meg = _merge_im(back, front, x, y)
    if save_path is not None:
        save_cv_image(save_path, meg)
    return meg


def merge_image_percentage_height_position(
    back,
    front,
    percentx,
    percenty,
    front_percentage_height,
    save_path=None,
    interpolation=cv2.INTER_AREA,
):
    back, front = _get_bf(back, front)
    front = cv2.easy_resize_image(
        front,
        width=None,
        height=int(back.shape[1] / 100 * front_percentage_height),
        percent=None,
        interpolation=interpolation,
    )
    x = int(back.shape[1] / 100 * percentx)
    y = int(back.shape[0] / 100 * percenty)
    meg = _merge_im(back, front, x, y)
    if save_path is not None:
        save_cv_image(save_path, meg)
    return meg


