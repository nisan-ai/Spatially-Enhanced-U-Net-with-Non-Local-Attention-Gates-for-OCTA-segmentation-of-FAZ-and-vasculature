def dice_loss(y_true, y_pred):
    return 1 - dice_coef(y_true, y_pred)


def focal_loss(y_true, y_pred, gamma=2.0, alpha=0.25,epsilon=1e-5):
    pt = y_true * y_pred
    gt = 1.0 - y_true
    p_t = tf.where(K.equal(y_true, 1), pt, gt)
    alpha_t = tf.where(K.equal(y_true, 1), alpha, 1.0 - alpha)
    ce_loss = -K.log(p_t + epsilon)
    weight = K.pow((1 - p_t), gamma)
    focal_loss = weight * alpha_t * ce_loss
    return focal_loss