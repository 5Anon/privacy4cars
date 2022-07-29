import pyodbc 
import time
cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:privacyforcars.database.windows.net,1433;Database=HistoricalDatabase;Uid=PfCCAdmin;Pwd={PrivacyForConnectedCars101#};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone()
while row: 
    print(row[0])
    row = cursor.fetchone()

cursor.execute('''
    CREATE TABLE OriginalDataset (
        car_id VARCHAR(10),
        META_DATA VARCHAR(32),
        GPS_Time VARCHAR(64),
        device_time VARCHAR(32),
        Longitude VARCHAR(32),
        Latitude VARCHAR(32),
        GPS_Speed VARCHAR(32),
        Horizontal_Dilution VARCHAR(32),
        Altitude VARCHAR(32),
        Bearing VARCHAR(32),
        G_x VARCHAR(32),
        G_y VARCHAR(32),
        G_z VARCHAR(32),
        G_calibrated VARCHAR(32),
        _0_100kph_Time_s VARCHAR(32),
        _0_100mph_Time_s VARCHAR(32),
        _0_200kph_Time_s VARCHAR(32),
        _0_30kph_Time_s VARCHAR(32),
        _0_60kph_Time_s VARCHAR(32),
        _1_4_Mile_Time_s VARCHAR(32),
        _1_8_Mile_Time_s VARCHAR(32),
        _100_0kph_Time_s VARCHAR(32),
        _100_200kph_Time_s VARCHAR(32),
        _40_60mph_Time_s VARCHAR(32),
        _60_0mph_Time_s VARCHAR(32),
        _60_120mph_Time_s VARCHAR(32),
        _60_130mph_Time_s VARCHAR(32),
        _60_80mph_Time_s VARCHAR(32),
        _80_100mph_Time_s VARCHAR(32),
        _80_120kph_Time_s VARCHAR(32),
        Absolute_Throttle_Pos_B_Percent VARCHAR(32),
        Acceleration_Sensor_Total_g VARCHAR(32),
        Acceleration_Sensor_X_axis_g VARCHAR(32),
        Acceleration_Sensor_Y_axis_g VARCHAR(32),
        Acceleration_Sensor_Z_axis_g VARCHAR(32),
        Accelerator_PedalPosition_D_Percent VARCHAR(32),
        Accelerator_PedalPosition_E_Percent VARCHAR(32),
        Accelerator_PedalPosition_F_Percent VARCHAR(32),
        Actual_engine_Percent_torque tinyint,
        Air_Fuel_Ratio_Commanded VARCHAR(32),
        Air_Fuel_Ratio_Measured VARCHAR(32),
        Alcohol_Fuel_Percentage VARCHAR(32),
        Ambient_air_temp VARCHAR(32),
        Android_device_Battery_Level VARCHAR(32),
        Average_trip_speed_whilst_moving_only_mph VARCHAR(32),
        Average_trip_speed_whilst_stopped_or_moving_mph VARCHAR(32),
        Barometer_on_Android_device_mb VARCHAR(32),
        Barometric_pressure_from_vehicle_psi VARCHAR(32),
        Boost_Pressure_Commanded_A_psi VARCHAR(32),
        Boost_Pressure_Commanded_B_psi VARCHAR(32),
        Boost_Pressure_Sensor_A_psi VARCHAR(32),
        Boost_Pressure_Sensor_B_psi VARCHAR(32),
        Catalyst_Temperature_Bank_1_Sensor_1_F VARCHAR(32),
        Catalyst_Temperature_Bank_1_Sensor_2_F VARCHAR(32),
        Catalyst_Temperature_Bank_2_Sensor_1_F VARCHAR(32),
        Catalyst_Temperature_Bank_2_Sensor_2_F VARCHAR(32),
        Charge_air_cooler_temperature_CACT_F VARCHAR(32),
        Commanded_Equivalence_Ratio_lambda VARCHAR(32),
        Cost_per_mile_km_Instant_dollar_per_m VARCHAR(32),
        Cost_per_mile_km_Trip_dollar_per_m VARCHAR(32),
        CO2_in_g_per_km_Average_g_per_km VARCHAR(32),
        CO2_in_g_per_km_Instantaneous_g_per_km VARCHAR(32),
        Distance_to_empty_Estimated_miles VARCHAR(32),
        Distance_travelled_since_codes_cleared_miles VARCHAR(32),
        Distance_travelled_with_MIL_per_CEL_lit_miles VARCHAR(32),
        DPF_Bank_1_Delta_Pressure_psi VARCHAR(32),
        DPF_Bank_1_Inlet_Pressure_psi VARCHAR(32),
        DPF_Bank_1_Inlet_Temperature_F VARCHAR(32),
        DPF_Bank_1_Outlet_Pressure_psi VARCHAR(32),
        DPF_Bank_1_Outlet_Temperature_F VARCHAR(32),
        DPF_Bank_2_Delta_Pressure_psi VARCHAR(32),
        DPF_Bank_2_Inlet_Pressure_psi VARCHAR(32),
        DPF_Bank_2_Inlet_Temperature_F VARCHAR(32),
        DPF_Bank_2_Outlet_Pressure_psi VARCHAR(32),
        DPF_Bank_2_Outlet_Temperature_F VARCHAR(32),
        Drivers_demand_engine_percent_torque_percent VARCHAR(32),
        EGR_Commanded_percent VARCHAR(32),
        EGR_Error_percent VARCHAR(32),
        Engine_Coolant_Temperature_degreeF VARCHAR(32),
        Engine_kW_At_the_wheels_kW VARCHAR(32),
        Engine_Load_percent VARCHAR(32),
        Engine_Load_Absolute_percent VARCHAR(32),
        Engine_Oil_Temperature_degreeF VARCHAR(32),
        Engine_reference_torque_Nm VARCHAR(32),
        Engine_RPM_rpm VARCHAR(32),
        Ethanol_Fuel_percent_percent VARCHAR(32),
        Evap_System_Vapour_Pressure_Pa VARCHAR(32),
        Exhaust_gas_temp_Bank_1_Sensor_1_degreeF VARCHAR(32),
        Exhaust_gas_temp_Bank_1_Sensor_2_degreeF VARCHAR(32),
        Exhaust_gas_temp_Bank_1_Sensor_3_degreeF VARCHAR(32),
        Exhaust_gas_temp_Bank_1_Sensor_4_degreeF VARCHAR(32),
        Exhaust_gas_temp_Bank_2_Sensor_1_degreeF VARCHAR(32),
        Exhaust_gas_temp_Bank_2_Sensor_2_degreeF VARCHAR(32),
        Exhaust_gas_temp_Bank_2_Sensor_3_degreeF VARCHAR(32),
        Exhaust_gas_temp_Bank_2_Sensor_4_degreeF VARCHAR(32),
        Exhaust_Pressure_Bank_1_psi VARCHAR(32),
        Exhaust_Pressure_Bank_2_psi VARCHAR(32),
        Fuel_cost_trip_cost VARCHAR(32),
        Fuel_flow_rate_per_hour_gal_per_hr VARCHAR(32),
        Fuel_flow_rate_per_minute_gal_per_min VARCHAR(32),
        Fuel_Level_From_Engine_ECU_percent VARCHAR(32),
        Fuel_pressure_psi VARCHAR(32),
        Fuel_Rail_Pressure_psi VARCHAR(32),
        Fuel_Rail_Pressure_relative_to_manifold_vacuum_psi VARCHAR(32),
        Fuel_Rate_direct_from_ECU_L_per_m VARCHAR(32),
        Fuel_Remaining_Calculated_from_vehicle_profile_percent VARCHAR(32),
        Fuel_Trim_Bank_1_Long_Term_percent VARCHAR(32),
        Fuel_Trim_Bank_1_Short_Term_percent VARCHAR(32),
        Fuel_Trim_Bank_2_Long_Term_percent VARCHAR(32),
        Fuel_Trim_Bank_2_Short_Term_percent VARCHAR(32),
        Fuel_trim_Bank_1_Sensor_1_percent VARCHAR(32),
        Fuel_trim_Bank_1_Sensor_2_percent VARCHAR(32),
        Fuel_trim_Bank_1_Sensor_3_percent VARCHAR(32),
        Fuel_trim_Bank_1_Sensor_4_percent VARCHAR(32),
        Fuel_trim_Bank_2_Sensor_1_percent VARCHAR(32),
        Fuel_trim_Bank_2_Sensor_2_percent VARCHAR(32),
        Fuel_trim_Bank_2_Sensor_3_percent VARCHAR(32),
        Fuel_trim_Bank_2_Sensor_4_percent VARCHAR(32),
        Fuel_used_trip_gal VARCHAR(32),
        GPS_Accuracy_ft VARCHAR(32),
        GPS_Altitude_ft VARCHAR(32),
        GPS_Bearing_degree VARCHAR(32),
        GPS_Latitude_degree VARCHAR(32),
        GPS_Longitude_degree VARCHAR(32),
        GPS_Satellites VARCHAR(32),
        GPS_vs_OBD_Speed_difference_mph VARCHAR(32),
        Horsepower__At_the_wheels_hp VARCHAR(32),
        Hybrid_Battery_Charge_percent_percent VARCHAR(32),
        Hybrid_or_EV_Battery_Remaining_Charge_percent VARCHAR(32),
        Hybrid_or_EV_Battery_State_of_Health_percent VARCHAR(32),
        Hybrid_or_EV_System_Battery_Current_A VARCHAR(32),
        Hybrid_or_EV_System_Battery_Power_W VARCHAR(32),
        Hybrid_or_EV_System_Battery_Voltage_V VARCHAR(32),
        Intake_Air_Temperature_degreeF VARCHAR(32),
        Intake_Manfold_Abs_Pressure_A_psi VARCHAR(32),
        Intake_Manfold_Abs_Pressure_B_psi VARCHAR(32),
        Intake_Manifold_Pressure_psi VARCHAR(32),
        Kilometers_Per_Litre_Instant_kpl VARCHAR(32),
        Kilometers_Per_Litre_Long_Term_Average_kpl VARCHAR(32),
        Litres_Per_100_Kilometer_Instant_l_per_100km VARCHAR(32),
        Litres_Per_100_Kilometer_Long_Term_Average_l_per_100km VARCHAR(32),
        Mass_Air_Flow_Rate_g_per_s VARCHAR(32),
        Mass_air_flow_sensor_A_g_per_s VARCHAR(32),
        Mass_air_flow_sensor_B_g_per_s VARCHAR(32),
        Miles_Per_Gallon_Instant_mpg VARCHAR(32),
        Miles_Per_Gallon_Long_Term_Average_mpg VARCHAR(32),
        NOx_Post_SCR_ppm VARCHAR(32),
        NOx_Pre_SCR_ppm VARCHAR(32),
        O2_Sensor1_Wide_Range_Current_mA VARCHAR(32),
        O2_Bank_1_Sensor_1_Voltage_V VARCHAR(32),
        O2_Bank_1_Sensor_1_Wide_Range_Equivalence_Ratio_lambda VARCHAR(32),
        O2_Bank_1_Sensor_1_Wide_Range_Voltage_V VARCHAR(32),
        O2_Bank_1_Sensor_2_Voltage_V VARCHAR(32),
        O2_Bank_1_Sensor_2_Wide_Range_Current_mA VARCHAR(32),
        O2_Bank_1_Sensor_2_Wide_Range_Equivalence_Ratio_lambda VARCHAR(32),
        O2_Bank_1_Sensor_2_Wide_Range_Voltage_V VARCHAR(32),
        O2_Bank_1_Sensor_3_Voltage_V VARCHAR(32),
        O2_Bank_1_Sensor_3_Wide_Range_Current_mA VARCHAR(32),
        O2_Bank_1_Sensor_3_Wide_Range_Equivalence_Ratio_lambda VARCHAR(32),
        O2_Bank_1_Sensor_3_Wide_Range_Voltage_V VARCHAR(32),
        O2_Bank_1_Sensor_4_Voltage_V VARCHAR(32),
        O2_Bank_1_Sensor_4_Wide_Range_Current_mA VARCHAR(32),
        O2_Bank_1_Sensor_4_Wide_Range_Equivalence_Ratio_lambda VARCHAR(32),
        O2_Bank_1_Sensor_4_Wide_Range_Voltage_V VARCHAR(32),
        O2_Bank_2_Sensor_1_Voltage_V VARCHAR(32),
        O2_Bank_2_Sensor_1_Wide_Range_Current_mA VARCHAR(32),
        O2_Bank_2_Sensor_1_Wide_Range_Equivalence_Ratio_lambda VARCHAR(32),
        O2_Bank_2_Sensor_1_Wide_Range_Voltage_V VARCHAR(32),
        O2_Bank_2_Sensor_2_Voltage_V VARCHAR(32),
        O2_Bank_2_Sensor_2_Wide_Range_Current_mA VARCHAR(32),
        O2_Bank_2_Sensor_2_Wide_Range_Equivalence_Ratio_lambda VARCHAR(32),
        O2_Bank_2_Sensor_2_Wide_Range_Voltage_V VARCHAR(32),
        O2_Bank_2_Sensor_3_Voltage_V VARCHAR(32),
        O2_Bank_2_Sensor_3_Wide_Range_Current_mA VARCHAR(32),
        O2_Bank_2_Sensor_3_Wide_Range_Equivalence_Ratio_lambda VARCHAR(32),
        O2_Bank_2_Sensor_3_Wide_Range_Voltage_V VARCHAR(32),
        O2_Bank_2_Sensor_4_Voltage_V VARCHAR(32),
        O2_Bank_2_Sensor_4_Wide_Range_Current_mA VARCHAR(32),
        O2_Bank_2_Sensor_4_Wide_Range_Equivalence_Ratio_lambda VARCHAR(32),
        O2_Bank_2_Sensor_4_Wide_Range_Voltage_V VARCHAR(32),
        Odometer_from_ECU_miles VARCHAR(32),
        Percentage_of_City_driving_percent VARCHAR(32),
        Percentage_of_Highway_driving_percent VARCHAR(32),
        Percentage_of_Idle_driving_percent VARCHAR(32),
        Positive_Kinetic_Energy_PKE_km_per_hr_squared VARCHAR(32),
        Relative_Accelerator_Pedal_Position_percent VARCHAR(32),
        Relative_Throttle_Position_percent VARCHAR(32),
        Run_time_since_engine_start_s VARCHAR(32),
        Speed_GPS_mph VARCHAR(32),
        Speed_OBD_mph VARCHAR(32),
        Throttle_Position_Manifold_percent VARCHAR(32),
        Timing_Advance_degree VARCHAR(32),
        Torque_Nm VARCHAR(32),
        Transmission_Temperature_Method_2_F VARCHAR(32),
        Trip_average_KPL_kpl VARCHAR(32),
        Trip_average_Litres_per_100_KM VARCHAR(32),
        Trip_average_MPG_mpg VARCHAR(32),
        Trip_Distance_miles VARCHAR(32),
        Trip_distance_stored_in_vehicle_profile_miles VARCHAR(32),
        Trip_Time_Since_journey_start_s VARCHAR(32),
        Trip_time_whilst_moving_s VARCHAR(32),
        Trip_time_whilst_stationary_s VARCHAR(32),
        Turbo_Boost_and_Vacuum_Gauge_psi VARCHAR(32),
        Voltage_Control_Module_V VARCHAR(32),
        Voltage_OBD_Adapter_V VARCHAR(32),
        Volumetric_Efficiency_Calculated_Percent VARCHAR(32)
        );
            ''')

cnxn.commit()