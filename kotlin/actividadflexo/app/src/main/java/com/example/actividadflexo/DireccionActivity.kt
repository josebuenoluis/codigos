package com.example.actividadflexo

import android.content.Intent
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
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_direccion)

        direccion = findViewById(R.id.direccionText)
        boton = findViewById(R.id.guardar)

        boton.setOnClickListener { activityMain() }

    }

    private fun activityMain(){
        var ip = direccion.text.toString()
        val intent = Intent(this,MainActivity::class.java)
        if(!ip.isNullOrEmpty()) {
            intent.putExtra("ip",ip)
        }
        startActivity(intent)
    }
}