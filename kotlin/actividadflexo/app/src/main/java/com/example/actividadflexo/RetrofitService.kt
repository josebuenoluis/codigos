package com.example.actividadflexo

import retrofit2.Retrofit
import retrofit2.Call
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Query

interface RetrofitService{
    @GET("rpc/Switch.Set")
     fun controlRele(
        @Query("id") id: Int,
        @Query("on") on: Boolean
    ): Call<Unit>
}

object ClienteRetrofit{
    fun crearServicioRetrofit(ip:String) : RetrofitService{
        return Retrofit.Builder()
            .baseUrl(ip)
            .addConverterFactory(GsonConverterFactory.create())
            .build().create(RetrofitService::class.java)
    }
}
