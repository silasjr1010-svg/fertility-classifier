"""Shared CBAM building block.

Keras 3 blocks auto-loading `Lambda` layers by default (arbitrary-code risk),
which breaks `load_model()` on any saved model that used one for the CBAM
spatial-attention pooling steps. `ChannelPool` replaces those Lambda calls
with a registered custom Layer subclass that serializes and reloads safely.

This exact class must be defined (or imported, as here) before
`tf.keras.models.load_model()` is called on any model that contains it —
used both in the training notebook and in app.py.
"""
import tensorflow as tf
from tensorflow.keras import layers


@tf.keras.utils.register_keras_serializable(package="CBAM")
class ChannelPool(layers.Layer):
    def __init__(self, pool_type="avg", **kwargs):
        super().__init__(**kwargs)
        self.pool_type = pool_type

    def call(self, inputs):
        if self.pool_type == "avg":
            return tf.reduce_mean(inputs, axis=-1, keepdims=True)
        return tf.reduce_max(inputs, axis=-1, keepdims=True)

    def get_config(self):
        config = super().get_config()
        config.update({"pool_type": self.pool_type})
        return config
