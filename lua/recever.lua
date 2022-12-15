already_set = false
param_set = false

function update()
  if param_set == false then
    local PARAM_TABLE_KEY = 72
    assert(param:add_table(PARAM_TABLE_KEY, "MON_", 30), 'could not add param table')
    assert(param:add_param(PARAM_TABLE_KEY, 1,  'NEAR', 0), 'could not add param1')
    gcs:send_text(0, "Set monitoring parameter")
    param_set = true
  end
  if param_set == true then
    local MON_NEAR = Parameter()
    MON_NEAR:init('MON_NEAR')
    local near_status = MON_NEAR:get()
    if near_status == 1 and already_set == false then
      local target_vel = Vector3f()
      target_vel:x(10)
      vehicle:set_target_velocity_NED(target_vel)
      already_set = true
    end
    if near_status == 0 and already_set == true then
      local target_vel = Vector3f()
      target_vel:x(-10)
      vehicle:set_target_velocity_NED(target_vel)
      already_set = false
    end 
  end
  return update, 1000
end
return update, 1000