package com.example.pro.persistencia

import android.content.Context
import android.os.Bundle
import androidx.activity.ComponentActivity
import android.content.SharedPreferences
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.pro.persistencia.ui.theme.PersistenciaTheme

class MainActivity : ComponentActivity() {
    lateinit var sharedPreferences: SharedPreferences
    lateinit var input1 : EditText
    lateinit var input2 : EditText
    lateinit var boton : Button
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        sharedPreferences = getSharedPreferences("misdatos",Context.MODE_PRIVATE)
        input1 = findViewById(R.id.clave)
        input2 = findViewById(R.id.valor)
        boton = findViewById(R.id.boton)
    }

    fun guardarDatos(){
        val editor = sharedPreferences.edit()
        val clave = input1.text.toString()
        val valor = input2.text.toString()
        editor.putString(clave,valor)
        editor.apply()
        Toast.makeText(this,"Datos guardados correctamente",Toast.LENGTH_SHORT).show()

    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    PersistenciaTheme {
        Greeting("Android")
    }
}