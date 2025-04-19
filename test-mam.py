import numpy as np 
import my_astro_module as mam 

#calculate the surface gravity of the Earth
gravity_earth = mam.g_surf(mam.m_earth, mam.r_earth)
print(gravity_earth)

Earth = {
	"name" : "Earth",
	"mass" : 1.0 * mam.m_earth,
	"radius" : 1.0 * mam.r_earth,
	"incident_flux" : 1.0 * mam.s_earth,
	"temperature" : 288.0,
	"albedo" : 0.31
}

Venus = {
	"name" : "Venus",
	"mass" : 0.815 * mam.m_earth,
	"radius" : 0.950 * mam.r_earth,
	"incident_flux" : 1.902 * mam.s_earth,
	"temperature" : 737.0,
	"albedo" : 0.77
}

k218b = {
	"name" : "k2-18b",
	"mass" : 8.63 * mam.m_earth,
	"radius" : 2.61 * mam.r_earth,
	"incident_flux" : 1.005 * mam.r_earth,
	"temperature" : 300.0,
	"albedo" : 0.31
}

#calculate the surface gravity by passing the dictionnary
gravity_earth = mam.g_surf2(Earth)
print(gravity_earth)

#show a sentence with the surface gracity of planets
mam.show_g_surf(Earth)
mam.show_g_surf(Venus)
mam.show_g_surf(k218b)

#show a sentence with temperatures of planets 
mam.show_temp_f(Earth)
mam.show_temp_f(Venus)
mam.show_temp_f(k218b)