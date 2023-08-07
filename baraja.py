num_jugadores = input('¿Cuántos jugadores participareis en esta partida?')
palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
numeros = ['1', '2', '3', '4', '5', '6', '7', 'SOTA', 'CABALLO', 'REY'] 
        
baraja_espanola = []

for palo in (palos):
    for numero in (numeros):
        carta = f'{numeros} de {palos}'
        baraja_espanola. append(carta)

print(baraja_espanola)            
        
        
    