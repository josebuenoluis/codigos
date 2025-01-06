 package com.example.actividadflexo

import android.content.ClipData.Item
import android.content.Intent
import android.content.res.Configuration
import android.graphics.drawable.Drawable
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.CompoundButton
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.Switch
import android.widget.Toast
import android.widget.ToggleButton
import androidx.activity.ComponentActivity
import androidx.activity.enableEdgeToEdge
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.lifecycle.lifecycleScope
import com.example.actividadflexo.ui.theme.ActividadflexoTheme
import kotlinx.coroutines.launch
import retrofit2.Retrofit

 class MainActivity : ComponentActivity() {
    private lateinit var linearPadre : LinearLayout
    private lateinit var togglebutton: ToggleButton
    private lateinit var switchButton : Switch
    private lateinit var linear1 : LinearLayout
    private lateinit var linear2 : LinearLayout
    private lateinit var clienteRetrofit : RetrofitService
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        linearPadre = findViewById(R.id.padre)
        linear1 = findViewById(R.id.linear1)
        linear2 = findViewById(R.id.linear2)

        togglebutton = findViewById(R.id.toggleFlexo)
        togglebutton.text = "Flexo Off"
        togglebutton.textOn = "Flexo On"
        togglebutton.textOff = "Flexo Off"
        togglebutton.setOnClickListener { cambioToggle() }

        switchButton = findViewById(R.id.switchButton)
        switchButton.setOnClickListener { cambioSwitch() }

    }

    private fun cambioSwitch(){
        if(switchButton.isChecked){
            togglebutton.isChecked = true
            peticion()
            mostrarToast("Switch activado correctamente")
        }else{
            togglebutton.isChecked = false
            mostrarToast("Switch desactivado correctamente")
        }

    }

    private fun mostrarToast(mensaje:String){
        Toast.makeText(this,mensaje,Toast.LENGTH_SHORT).show()
    }

    private fun cambioToggle(){
        if(togglebutton.isChecked){
            switchButton.isChecked = true
            peticion()
            mostrarToast("Switch activado correctamente")
        }else{
            switchButton.isChecked = false
            mostrarToast("Switch desactivado correctamente")
        }
    }

    private fun activityDireccion(){
        val intent = Intent(this,DireccionActivity::class.java)
        startActivity(intent)
    }

    private fun peticion(){
        var ip = intent.getStringExtra("ip")
        ip = "http://$ip/"
        println(ip)
        clienteRetrofit = ClienteRetrofit.crearServicioRetrofit(ip)
        lifecycleScope.launch{
            try {
                val response = clienteRetrofit.controlRele()
                println("Conexion exitosa")
            } catch (e: Exception) {
                println("Conexion fallida")
            }
        }

    }

    override fun onMenuItemSelected(featureId: Int, item: MenuItem): Boolean {
        when(item.itemId){
            R.id.naranja -> {
                println("Presiono naranja")
                linear1.setBackgroundColor(getColor(R.color.naranjita))
            }
            R.id.azul -> {
                println("Presiono azul")
                linear2.setBackgroundColor(getColor(R.color.azulito))
            }
            R.id.blanco -> {
                println("Presiono blanco")
                linear1.setBackgroundColor(getColor(R.color.white))
                linear2.setBackgroundColor(getColor(R.color.white))
            }
            R.id.direccion -> {
                println("Presiono busqueda")
                activityDireccion()
            }
        }
        return true
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu,menu)
        return true
    }

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)
        if (newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE){
            linearPadre.orientation = LinearLayout.HORIZONTAL
        }else{
            linearPadre.orientation = LinearLayout.VERTICAL
        }
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
    ActividadflexoTheme {
        Greeting("Android")
    }
}