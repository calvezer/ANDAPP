package com.example.test_addnotes;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.PopupWindow;
import android.widget.RelativeLayout;


public class MainActivity extends AppCompatActivity {

    private Button test;
    private PopupWindow popupwindow ;
    private LayoutInflater layoutinflater ;
    private RelativeLayout relativelayout ;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        test = findViewById(R.id.Btn_addnotes);
        relativelayout = findViewById(R.id.relativeLayout);
        //rellayout = findViewById(R.id.relativeLayout);

        test.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                layoutinflater = (LayoutInflater) getApplicationContext().getSystemService(LAYOUT_INFLATER_SERVICE);
                ViewGroup container = (ViewGroup) layoutinflater.inflate(R.layout.popupwindow, null);

                popupwindow = new PopupWindow(container,800,800, true);
                popupwindow.showAtLocation(relativelayout,Gravity.NO_GRAVITY,50,450);

                container.setOnTouchListener(new View.OnTouchListener() {
                    @Override
                    public boolean onTouch(View v, MotionEvent event) {
                        popupwindow.dismiss();
                        return true;
                    }
                });
            }
        });
    }

}