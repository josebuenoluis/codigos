package com.example.pro.toast

import android.os.Bundle
import android.view.Gravity
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.pro.toast.ui.theme.ToastTheme


class MainActivity : ComponentActivity() {
    private lateinit var botonToast : Any
    private lateinit var toast : Toast
    private lateinit var input : EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        toast = Toast(this)
        toast.setGravity(Gravity.TOP,200,500)
        botonToast = findViewById<Button?>(R.id.boton).setOnClickListener { mostrarMensaje() }
        input = findViewById(R.id.input)
    }

    fun cambiarMensajes(){
        val texto = input.text.toString()
        if (texto != ""){
            toast.setText(texto)
        }
    }

    fun mostrarMensaje(){
        cambiarMensajes()
        toast.duration = Toast.LENGTH_LONG
        toast.show()
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
    ToastTheme {
        Greeting("Android")
    }
}