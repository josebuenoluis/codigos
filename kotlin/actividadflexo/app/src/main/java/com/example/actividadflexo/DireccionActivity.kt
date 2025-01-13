package com.example.actividadflexo

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.os.Bundle
import android.widget.EditText
import android.widget.Button
import androidx.activity.ComponentActivity
import androidx.activity.enableEdgeToEdge
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class DireccionActivity : ComponentActivity() {
    private lateinit var direccion : EditText
    private lateinit var boton : Button
    private lateinit var archivo : SharedPreferences
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_direccion)

        direccion = findViewById(R.id.direccionText)
        boton = findViewById(R.id.guardar)
        archivo = getSharedPreferences("direccion", Context.MODE_PRIVATE)
        var ip = archivo.getString("ip","")
        direccion.setText(ip)

        boton.setOnClickListener { activityMain() }

    }

    private fun guardar(ip:String){
        val editor = archivo.edit()
        editor.putString("ip",ip)
        editor.apply()

    }

    private fun activityMain(){
        var ip = direccion.text.toString()
        val intent = Intent(this,MainActivity::class.java)
        if(!ip.isNullOrEmpty()) {
            guardar(ip)
        }
        startActivity(intent)
    }
}