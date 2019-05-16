package com.example.app;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    Spinner spin;
    List<String> list;
    ArrayAdapter adapter;//声明一个数组适配器，用于将列表中的数值与Spinner挂件绑定


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        spin = (Spinner)findViewById(R.id.spinner);
        list = new ArrayList<String>();
        list.add("spinner 子项1");
        list.add("spinner 子项2");
        list.add("spinner 子项3");

        adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_checked, list);
        adapter.setDropDownViewResource(android.R.layout.simple_dropdown_item_1line);
        spin.setAdapter(adapter);

        spin.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

            }
        });
    }
}
