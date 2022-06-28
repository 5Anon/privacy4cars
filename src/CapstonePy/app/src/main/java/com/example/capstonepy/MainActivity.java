package com.example.capstonepy;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.SwitchCompat;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import android.widget.CompoundButton;
import android.widget.TextView;
//Python libs
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {

    //Displays text on GUI for testing
    TextView textView;

    // Initialize variable
    SwitchCompat switchCompat;
    SwitchCompat switchCompat2;
    SwitchCompat switchCompat3;
    SwitchCompat switchCompat4;
    SwitchCompat switchCompat5;

    Button btNext,btExit;

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

        PyObject pyobj = py.getModule("myscript");

        PyObject obj = pyobj.callAttr("main");

        textView.setText(obj.toString());
        //End Python Function


        // Assign variable
        switchCompat=findViewById(R.id.switch_compat);
        switchCompat2=findViewById(R.id.switch_compat2);
        switchCompat3=findViewById(R.id.switch_compat3);
        switchCompat4=findViewById(R.id.switch_compat4);
        switchCompat5=findViewById(R.id.switch_compat5);

        btNext=findViewById(R.id.bt_next);
        btExit=findViewById(R.id.bt_exit);

        // Save switch state in shared preferences
        SharedPreferences sharedPreferences=getSharedPreferences("save",MODE_PRIVATE);
        switchCompat.setChecked(sharedPreferences.getBoolean("location_privacy_setting",true));
        switchCompat2.setChecked(sharedPreferences.getBoolean("vision_privacy_setting",true));
        switchCompat3.setChecked(sharedPreferences.getBoolean("maintenance_privacy_setting",true));
        switchCompat4.setChecked(sharedPreferences.getBoolean("driving_privacy_setting",true));
        switchCompat5.setChecked(sharedPreferences.getBoolean("bluetooth_privacy_setting",true));

        switchCompat.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (switchCompat.isChecked())
                {
                    // When switch checked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("location_privacy_setting",true);
                    editor.apply();
                    switchCompat.setChecked(true);
                    textView.setText("Location Switch Enabled");
                }
                else
                {
                    // When switch unchecked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("location_privacy_setting",false);
                    editor.apply();
                    switchCompat.setChecked(false);
                    textView.setText("Location Switch Disabled");
                }
            }
        });

        switchCompat2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (switchCompat2.isChecked())
                {
                    // When switch checked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("vision_privacy_setting",true);
                    editor.apply();
                    switchCompat2.setChecked(true);
                    textView.setText("Vision Switch Enabled");
                }
                else
                {
                    // When switch unchecked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("vision_privacy_setting",false);
                    editor.apply();
                    switchCompat2.setChecked(false);
                    textView.setText("Vision Switch Disabled");
                }
            }
        });

        switchCompat3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (switchCompat3.isChecked())
                {
                    // When switch checked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("maintenance_privacy_setting",true);
                    editor.apply();
                    switchCompat3.setChecked(true);
                    textView.setText("Maintenance Switch Enabled");
                }
                else
                {
                    // When switch unchecked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("maintenance_privacy_setting",false);
                    editor.apply();
                    switchCompat3.setChecked(false);
                    textView.setText("Maintenance Switch Disabled");
                }
            }
        });

        switchCompat4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (switchCompat4.isChecked())
                {
                    // When switch checked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("driving_privacy_setting",true);
                    editor.apply();
                    switchCompat4.setChecked(true);
                    textView.setText("Driving Behavior Switch Enabled");
                }
                else
                {
                    // When switch unchecked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("driving_privacy_setting",false);
                    editor.apply();
                    switchCompat4.setChecked(false);
                    textView.setText("Driving Behavior Switch Disabled");
                }
            }
        });

        switchCompat5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (switchCompat5.isChecked())
                {
                    // When switch checked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("bluetooth_privacy_setting",true);
                    editor.apply();
                    switchCompat5.setChecked(true);
                    textView.setText("Bluetooth Switch Enabled");
                }
                else
                {
                    // When switch unchecked
                    SharedPreferences.Editor editor=getSharedPreferences("save",MODE_PRIVATE).edit();
                    editor.putBoolean("bluetooth_privacy_setting",false);
                    editor.apply();
                    switchCompat5.setChecked(false);
                    textView.setText("Bluetooth Switch Disabled");
                }
            }
        });

        btNext.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Go to next activity
                Intent intent=new Intent(MainActivity.this,MainActivity2.class);
                startActivity(intent);
            }
        });
        btExit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Close the app
                MainActivity.this.finishAffinity();
            }
        });
    }
}




//import androidx.appcompat.app.AppCompatActivity;
//import androidx.appcompat.widget.SwitchCompat;
//
//import android.content.Intent;
//import android.content.SharedPreferences;
//import android.os.Bundle;
//import android.service.autofill.FillEventHistory;
//import android.os.Bundle;
//import android.view.View;
//import android.widget.Button;
//
//import android.widget.TextView;
//
//import com.chaquo.python.PyObject;
//import com.chaquo.python.Python;
//import com.chaquo.python.android.AndroidPlatform;
//import com.google.android.material.switchmaterial.SwitchMaterial;
//
//public class MainActivity extends AppCompatActivity
//{
//
//    TextView textView;
//
//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_main);
//
//        textView = (TextView)findViewById(R.id.textview);
//
//        if (! Python.isStarted()) {
//            Python.start(new AndroidPlatform(this));
//        }
//
//        Python py = Python.getInstance();
//
//        PyObject pyobj = py.getModule("myscript");
//
//        PyObject obj = pyobj.callAttr("main");
//
//        textView.setText(obj.toString());
//
//    }
//
//    private void loadSharedPreferences()
//    {
//        SharedPreferences sharedPreferences = getSharedPreferences()
//    }
//
//
//
//}

