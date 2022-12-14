already_set = false

function update() 
  local original_location = ahrs:get_position()
  flight_mode = vehicle:get_mode()
  if flight_mode == 111 and already_set == false then
    gcs:send_text(0, "HOGEHOGE")
    vehicle:set_target_location(current:lat()-0.0001,current:lng(),current:alt())
    already_set = true
  end
  if flight_mode == 4 and already_set == true then
    gcs:send_text(0, "Rest Monitoring")
    vehicle:set_target_location(current:lat()+0.0001,current:lng(),current:alt())
    already_set = false
  end
  return update, 1000
end
return update, 1000