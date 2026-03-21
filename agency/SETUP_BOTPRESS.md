# 🚀 SETUP: Agencia Automatización - Restaurantes Ecuador

## Paso 1: Crear cuenta Botpress
1. Ir a: https://botpress.com
2. Click "Get Started Free"
3. Crear cuenta con Google o email
4. Verified email

## Paso 2: Crear Workspace
1. New Workspace → "Agencia Automatización"
2. Workspace name: "AgenciaAuto"

## Paso 3: Crear Bot "Restaurant Bot"
1. New Bot → "Restaurant Bot"
2. Template: Start from Scratch
3. Bot name: "Restaurants EC"

## Paso 4: Configurar WhatsApp Channel
1. Ir a Channels → WhatsApp
2. Seguir instrucciones para conectar WhatsApp Business API
3. Opcional: Usar Botpress Cloud (gratis hasta 100 msgs)

## Paso 5: Crear Flow de Pedidos
```
START → MENU → ASK_ITEM → CONFIRM → COLLECT_INFO → ORDER_COMPLETE
```

### Node: MENU
```
Content:
"¡Hola! 👋 Soy el asistente de [NOMBRE RESTAURANTE]. 
¿Qué te gustaría ordenar?

🍔 Hamburguesas
🍕 Pizzas
🥗 Ensaladas
🍹 Bebidas

Responde con el número o nombre."
```

### Node: ASK_ITEM
Content según selección del cliente

### Node: CONFIRM
```
Content:
"Perfecto! Tu pedido:
[item]
Precio: [precio]

¿Confirmas? Responde SI o NO"
```

### Node: COLLECT_INFO
```
Content:
"Ingresa tu nombre y dirección para la entrega:"
```

### Node: ORDER_COMPLETE
```
Content:
"✅ ¡Pedido confirmado!

Resumen:
[item]
Cliente: [nombre]
Dirección: [dirección]

Te llega en [tiempo]. 
¡Gracias por tu orden!"
```

## Paso 6: Integrar Google Sheets (para recibir pedidos)
1. Crear spreadsheet "Pedidos_Restaurante"
2. Columnas: Timestamp, Cliente, Item, Precio, Dirección, Estado
3. En Botpress: Add "Google Sheets" integration
4. Configurar para que cada pedido se registre

## Paso 7: Testing
1. Enviar mensaje de prueba al bot
2. Verificar que responde correctamente
3. Verificar que datos llegan a Google Sheets

## Recursos
- Botpress Docs: https://botpress.com/docs
- WhatsApp Business API: https://business.whatsapp.com/developers/developers-hub
- Tutoriales: YouTube "Botpress restaurant bot"

## Tiempo estimado: 2-3 horas
