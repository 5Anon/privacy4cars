package com.example.capstonepy;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.SwitchCompat;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.View;
import android.widget.Button;

import android.widget.TextView;

//Information popup
import android.widget.Toast;

//Python libs
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

//Button
import android.content.Intent;

//timer
import java.util.Locale;
import java.util.concurrent.TimeUnit;




public class MainActivity extends AppCompatActivity {

    //String src = "/storage/emulated/0/Download/trackLog-2022-Jun-12_20-42-17.csv";
    //String dst = "/data/data/com.example.capstonepy/files/test.csv";


    //Displays output on GUI for testing
    TextView textView;

    // Initialize variable for switches
    SwitchCompat switchLocation;
    SwitchCompat switchVision;
    SwitchCompat switchMaintenance;
    SwitchCompat switchDriving;
    //SwitchCompat switchBluetooth;

    //Button btNext,btExit;
    Button btNext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        textView = (TextView)findViewById(R.id.textview);

        //Python function
        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        Python py = Python.getInstance();

        //PyObject pyobj = py.getModule("myscript");

        //PyObject obj = pyobj.callAttr("main");

        //textView.setText(obj.toString());

        //End Python Function

        //Timer
        long duration = TimeUnit.SECONDS.toMillis(10000);

        //Initialize Timer
        new CountDownTimer(duration, 1000) {
            @Override
            public void onTick(long l) {

                String sDuration = String.format(Locale.ENGLISH, "%02d : %02d"
                ,TimeUnit.MILLISECONDS.toMinutes(l)
                        ,TimeUnit.MILLISECONDS.toSeconds(l) -
                                TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(l)));
                //textView.setText(sDuration);
            }

            @Override
            public void onFinish() {

                boolean processUpdate = switchLocation.isChecked() || switchVision.isChecked() || switchMaintenance.isChecked() || switchDriving.isChecked();

                //Information balloon popup
                Toast.makeText(getApplicationContext(), "Collecting and Sending Data....",Toast.LENGTH_LONG).show();

                if (processUpdate) {
                    PyObject pyobj = py.getModule("myscript");
                    PyObject obj = pyobj.callAttr("main");
                    textView.setText(obj.toString());
                }



//                if (switchLocation.isChecked()){
//                    PyObject obj = pyobj.callAttr("locationFunction");
//                }
//
//                if (switchVision.isChecked()){
//                    PyObject obj = pyobj.callAttr("visionFunction");
//                }
//
//                if (switchMaintenance.isChecked()){
//                    PyObject obj = pyobj.callAttr("maintenanceFunction");
//                }
//
//                if (switchDriving.isChecked()){
//                    PyObject obj = pyobj.callAttr("drivingFunction");
//                    //textView.setText(obj.toString());
//                }

                this.start();
                //textView.setVisibility((View.GONE));

                //, "Countdown Timer has ended", Toast.LENGTH_LONG.show());

            }
        }.start();

        //End Timer


        // Assign variable
        switchLocation=findViewById(R.id.switch_location);
        switchVision=findViewById(R.id.switch_vision);
        switchMaintenance=findViewById(R.id.switch_maintenance);
        switchDriving=findViewById(R.id.switch_driving);
        //switchBluetooth=findViewById(R.id.switch_bluetooth);

        //Testing buttons
        btNext=findViewById(R.id.bt_next);
        //btExit=findViewById(R.id.bt_exit);

        // Save switch state in shared preferences
        SharedPreferences sharedPreferences=getSharedPreferences("save",MODE_PRIVATE);
        switchLocation.setChecked(sharedPreferences.getBoolean("location_privacy_setting",false));
        switchVision.setChecked(sharedPreferences.getBoolean("vision_privacy_setting",false));
        switchMaintenance.setChecked(sharedPreferences.getBoolean("maintenance_privacy_setting",false));
        switchDriving.setChecked(sharedPreferences.getBoolean("driving_privacy_setting",false));
        //switchBluetooth.setChecked(sharedPreferences.getBoolean("bluetooth_privacy_setting",true));

        switchLocation.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (switchLocation.isChecked())
                {
                    // When switch checked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("location_privacy_setting",true);
                    editor.apply();
                    switchLocation.setChecked(true);
                    textView.setText("Opted-in to share Location Data");

//                    PyObject obj = pyobj.callAttr("locationFunction");
//                    textView.setText(obj.toString());
                }
                else
                {
                    // When switch unchecked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("location_privacy_setting",false);
                    editor.apply();
                    switchLocation.setChecked(false);
                    textView.setText("Opted-out to share Location Data");

                }
            }
        });

        switchVision.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (switchVision.isChecked())
                {
                    // When switch checked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("vision_privacy_setting",true);
                    editor.apply();
                    switchVision.setChecked(true);
                    textView.setText("Opted-in to share Vision Data");

//                    PyObject obj = pyobj.callAttr("visionFunction");
//                    textView.setText(obj.toString());
                }
                else
                {
                    // When switch unchecked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("vision_privacy_setting",false);
                    editor.apply();
                    switchVision.setChecked(false);
                    textView.setText("Opted-out to share Vision Data");
                }
            }
        });

        switchMaintenance.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (switchMaintenance.isChecked())
                {
                    // When switch checked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("maintenance_privacy_setting",true);
                    editor.apply();
                    switchMaintenance.setChecked(true);
                    textView.setText("Opted-in to share Maintenance Data");
//
//                    PyObject obj = pyobj.callAttr("maintenanceFunction");
//                    textView.setText(obj.toString());
                }
                else
                {
                    // When switch unchecked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("maintenance_privacy_setting",false);
                    editor.apply();
                    switchMaintenance.setChecked(false);
                    textView.setText("Opted-out to share Maintenance Data");
                }
            }
        });

        switchDriving.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (switchDriving.isChecked())
                {
                    // When switch checked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("driving_privacy_setting",true);
                    editor.apply();
                    switchDriving.setChecked(true);
                    textView.setText("Opted-in to share Driving Behavior Data");

//                    PyObject obj = pyobj.callAttr("drivingBehaviorFunction");
//                    textView.setText(obj.toString());
                }
                else
                {
                    // When switch unchecked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("driving_privacy_setting",false);
                    editor.apply();
                    switchDriving.setChecked(false);
                    textView.setText("Opted-out to share Driving Behavior Data");

                }
            }
        });

//        switchBluetooth.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                if (switchBluetooth.isChecked())
//                {
//                    // When switch checked
//                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
//                    editor.putBoolean("bluetooth_privacy_setting",true);
//                    editor.apply();
//                    switchBluetooth.setChecked(true);
//                    textView.setText("Bluetooth Switch Enabled");
//
//                    PyObject obj = pyobj.callAttr("bluetoothFunction");
//                    textView.setText(obj.toString());
//                }
//                else
//                {
//                    // When switch unchecked
//                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
//                    editor.putBoolean("bluetooth_privacy_setting",false);
//                    editor.apply();
//                    switchBluetooth.setChecked(false);
//                    textView.setText("Bluetooth Switch Disabled");
//                }
//            }
//        });


        //Test buttons functions
        btNext.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Go to next activity

                PyObject pyobj = py.getModule("myscript");

                PyObject obj = pyobj.callAttr("main");

                textView.setText(obj.toString());

                //Intent intent=new Intent(MainActivity.this,MainActivity2.class);
                //startActivity(intent);
            }
        });
//        btExit.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                // Close the app
//                MainActivity.this.finishAffinity();
//            }
//        });
    }
}

