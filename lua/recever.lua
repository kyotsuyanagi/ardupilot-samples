function update () 
    flight_mode = vehicle:get_mode()
    if flight_mode == 111 then
      target_vel = Vector3f()
      target_vel:y(2)
      gcs:send_text(0, "HOGEHOGE")
    end
    gcs:send_text(0, "LUA Monitoring")
    return update, 1000
  end
  return update, 1000