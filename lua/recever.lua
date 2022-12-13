already_set = false

function avoid()
  local current = ahrs:get_position()
  local item = mavlink_mission_item_int_t()
  mission:clear()
  item:command(WAYPOINT)
  item:x(current:lat() + 0.001)
  item:y(current:lng())
  item:z(current:alt())
  
  if not mission:set_item(0, item) then
    gcs:send_text(4, "avoiding mission is set")
    return false
  end
  return true
end

function return_orginal()
  local current = ahrs:get_position()
  local item = mavlink_mission_item_int_t()
  mission:clear()
  item:command(WAYPOINT)
  item:x(current:lat() - 0.001)
  item:y(current:lng())
  item:z(current:alt())
  
  if not mission:set_item(0, item) then
    gcs:send_text(4, "returning mission is set")
    return false
  end
  return true
end


function update () 
  flight_mode = vehicle:get_mode()
  if flight_mode == 111 and already_set == false then
    gcs:send_text(0, "HOGEHOGE")
    return avoid(), 1000
  end
  if flight_mode == "GUIDED" and already_set == true then
    already_set = false
    gcs:send_text(0, "Rest Monitoring")
  end
  return update, 1000
end
return update, 1000