att_unet_model.compile(optimizer=Adam(learning_rate=1e-3), loss=total_loss,
history = att_unet_model.fit(X_train, y_train, verbose=1, batch_size=batch_size, shuffle=False, epochs=400,
att_unet_model.compile(optimizer=Adam(learning_rate=1e-2), loss=total_loss,
'''history = att_unet_model.fit(train_generator, verbose=1, batch_size=batch_size, steps_per_epoch=steps_per_epoch, shuffle=False, epochs=200,
history = att_unet_model.fit(
att_unet_model.compile(optimizer=Adam(learning_rate=1e-3), loss=total_loss,
'''history = att_unet_model.fit(train_generator, verbose=1, batch_size=batch_size, steps_per_epoch=steps_per_epoch, shuffle=False, epochs=200,
history = att_unet_model.fit(