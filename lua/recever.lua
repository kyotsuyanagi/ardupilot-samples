local target_vel = Vector3f()
function update () 
  flight_mode = vehicle:get_mode()
  if flight_mode = "HOGEHOGE" then
    target_vel:y(2) #or target_vel:x(2)
    gcs:send_text(0, "HOGEHOGE")
  end
  gcs:send_text(0, "LUA Monitoring")
  return update, 1000
end
return update, 1000