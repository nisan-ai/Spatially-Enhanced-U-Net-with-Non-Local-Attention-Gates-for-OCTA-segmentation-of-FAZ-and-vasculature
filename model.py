def conv_block(x, filter_size, size, dropout, batch_norm=False):
    conv = layers.Conv2D(size, (filter_size, filter_size), padding="same")(x)
    if batch_norm is True:
        conv = layers.BatchNormalization(axis=3)(conv)
    conv = layers.Activation("relu")(conv)


def repeat_elem(tensor, rep):
    # lambda function to repeat Repeats the elements of a tensor along an axis
    # by a factor of rep.
    # If tensor has shape (None, 256,256,3), lambda will return a tensor of shape
    # (None, 256,256,6), if specified axis=3 and rep=2.


def gating_signal(input, out_size, batch_norm=False):
    """
    resize the down layer feature map into the same dimension as the up layer feature map
    using 1x1 conv
    :return: the gating feature map with the same dimension of the up layer feature map
    """
    x = layers.Conv2D(out_size, (1, 1), padding='same')(input)
    if batch_norm:
        x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    return x


def attention_block(x, gating, inter_shape):
    shape_x = K.int_shape(x)
    shape_g = K.int_shape(gating)


def non_local_attention_gate(x, gating, inter_shape):
    shape_x = K.int_shape(x)
    shape_g = K.int_shape(gating)
    batch_size = tf.shape(x)[0]


def Attention_UNet(input_shape, NUM_CLASSES=1, dropout_rate=0.0, batch_norm=True):
    '''
    Attention UNet,


def channel_attention(x, gating, inter_shape):
    shape_x = x.get_shape().as_list()
    shape = gating.get_shape().as_list()
    gating = tf.keras.layers.UpSampling2D(size=(shape_x[1] // gating.shape[1], shape_x[2] // gating.shape[2]))(gating)
    # Squeeze spatial features using average pooling and max pooling
    Fcavg = tf.reduce_mean(gating, axis=[1, 2], keepdims=True)  # Average pooling
    Fcmax = tf.reduce_max(gating, axis=[1, 2], keepdims=True)  # Max pooling


def spatial_attention(x, gating, inter_shape, kernel_size=7):
    # Apply average pooling, max pooling, and 1x1 convolution to the gating signal
    # Encoder spatial attention
    shape_x = x.get_shape().as_list()
    shape = gating.get_shape().as_list()
    gating = tf.keras.layers.UpSampling2D(size=(shape_x[1] // gating.shape[1], shape_x[2] // gating.shape[2]))(gating)


def Spatial_Channel_gated_Attention(x, gating, inter_shape):
    channel_output = channel_attention(x, gating, inter_shape)
    spatial_output = spatial_attention(x, gating, inter_shape)
    final_x = tf.multiply(channel_output, spatial_output)


def global_channel_attention(x, in_channels, reduction=16):
    #avg_pool = tf.reduce_mean(x, axis=[1, 2], keepdims=True)
    avg_pool = tf.keras.layers.GlobalAveragePooling2D(keepdims=True)(x)
    tf.print("Shape of avg_pool:", K.int_shape(avg_pool))
    cse = tf.keras.layers.Conv2D(in_channels // reduction, (1, 1), activation='relu')(avg_pool)
    tf.print("Shape of cse:", K.int_shape(cse))
    cse = tf.keras.layers.Conv2D(in_channels, (1, 1), activation='sigmoid')(cse)
    tf.print("Shape of cse", K.int_shape(cse))


def spatial_attention_1(x):
    sse = tf.keras.layers.Conv2D(1, (1, 1), activation='sigmoid')(x)
    tf.print("Shape of sse:", K.int_shape(sse))


def scse_module(x, in_channels, reduction=16):
    cse_output = global_channel_attention(x, in_channels, reduction)
    tf.print("Shape of cse_output:", K.int_shape(cse_output))
    sse_output = spatial_attention_1(x)
    tf.print("Shape of sse_output", K.int_shape(sse_output))
    total = x * cse_output + x * sse_output
    return x * cse_output + x * sse_output


def res_conv_block(x, kernelsize, filters, dropout, batchnorm=False):
    conv1 = layers.Conv2D(filters, (kernelsize, kernelsize), kernel_initializer='he_normal', padding='same')(x)
    if batchnorm is True:
        conv1 = layers.BatchNormalization(axis=3)(conv1)
    conv1 = layers.Activation('relu')(conv1)    
    conv2 = layers.Conv2D(filters, (kernelsize, kernelsize), kernel_initializer='he_normal', padding='same')(conv1)
    if batchnorm is True:
        conv2 = layers.BatchNormalization(axis=3)(conv2)
        conv2 = layers.Activation("relu")(conv2)
    if dropout > 0:
        conv2 = layers.Dropout(dropout)(conv2)
        

def spatial_attention_encode(x, inter_shape, kernel_size=7):
    # Apply average pooling, max pooling, and 1x1 convolution to the gating signal
    # Encoder spatial attention
    shape_x = x.get_shape().as_list()
    

def channel_attention_encode(x, inter_shape):
    shape_x = x.get_shape().as_list()
    

def resatt_block(x, num_layers, filter_size, size, dropout, batch_norm=False):
    J = 4
    