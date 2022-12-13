already_set == false

function update () 
  flight_mode = vehicle:get_mode()
  if flight_mode == 111 and already_set == false then
    gcs:send_text(0, "HOGEHOGE")
    local target_vel = Vector3f()
    target_vel:x(2)
    vehicle:set_target_velocity_NED(target_vel))
    already_set = true
  end
  if flight_mode == 4 and already_set == true then
    already_set = false
    gcs:send_text(0, "Rest Monitoring")
    local target_vel = Vector3f()
    target_vel:x(-2)
    vehicle:set_target_velocity_NED(target_vel))
  end
  return update, 1000
end
return update, 1000