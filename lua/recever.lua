already_set = false
WAYPOINT = 16
function avoid()
  local current = ahrs:get_position()
  local item = mavlink_mission_item_int_t()
  mission:clear()
  item:command(WAYPOINT)
  item:x(current:lat())
  item:y(current:lng())
  item:z(current:alt()+10)

  if mission:set_item(0, item) then
    gcs:send_text(4, "avoiding mission is set")
    mission:start(0)
    gcs:send_text(4, "avoiding mission is executed")
    return true
  else
    gcs:send_text(4, "avoiding mission is failed to set")
    return false
  end
end

function return_orginal()
  local current = ahrs:get_position()
  local item = mavlink_mission_item_int_t()
  mission:clear()
  item:command(WAYPOINT)
  item:x(current:lat())
  item:y(current:lng())
  item:z(current:alt()-10)
  
  if mission:set_item(0, item) then
    gcs:send_text(4, "returning mission is set")
    mission:start(0)
    gcs:send_text(4, "returning mission is executed")
    return true
  else
    gcs:send_text(4, "returning mission is failed to set")
    return false
  end
end


function update () 
  flight_mode = vehicle:get_mode()
  if flight_mode == 111 and already_set == false then
    gcs:send_text(0, "HOGEHOGE")
    if avoid() then
      gcs:send_text(4, "Avoiding")
      already_set = true
    end
  end
  if flight_mode == 4 and already_set == true then
    if return_orginal() then
      already_set = false
      gcs:send_text(0, "Rest Monitoring")
    end
  end
  return update, 1000
end
return update, 1000