# TecnoMóvil Colombia - Landing Page Spec

## 1. Concept & Vision

Tienda online de celulares premium para el mercado colombiano. Transmite confianza, modernidad y tecnología de vanguardia. La experiencia debe sentirse como entrar a una tienda física de alta gama pero con la comodidad de comprar desde casa. Énfasis en conversión: cada elemento guía hacia la compra.

## 2. Design Language

### Aesthetic Direction
Premium tech retail - inspirado en Apple Store meets modern e-commerce. Limpio, espacioso, con acentos de color vibrantes que guidan la atención.

### Color Palette
- **Primary:** #2563EB (Electric Blue)
- **Secondary:** #7C3AED (Violet)
- **Accent:** #06B6D4 (Cyan)
- **Success:** #10B981 (Green for discounts/savings)
- **Background:** #F8FAFC (Light) / #0F172A (Dark sections)
- **Surface:** #FFFFFF
- **Text Primary:** #1E293B
- **Text Secondary:** #64748B
- **Danger:** #EF4444

### Typography
- **Headings:** Inter (700, 600) - clean, modern, highly legible
- **Body:** Inter (400, 500) - excellent screen readability
- **Prices:** Space Grotesk (700) - distinctive for numbers
- **Fallbacks:** system-ui, sans-serif

### Spatial System
- Base unit: 4px
- Section padding: 80px vertical (desktop), 48px (mobile)
- Card padding: 24px
- Grid gap: 24px
- Border radius: 12px (cards), 8px (buttons), 24px (large sections)

### Motion Philosophy
- Micro-interactions: 200ms ease-out
- Page transitions: 300ms ease-in-out
- Hover lifts: translateY(-4px) with shadow increase
- Stagger animations for product grids: 50ms delay between items
- Cart slide-in: 400ms cubic-bezier(0.16, 1, 0.3, 1)

### Visual Assets
- Icons: Lucide Icons (CDN)
- Product images: Unsplash phone images
- Hero: Abstract tech gradient or phone mockup
- Decorative: Subtle grid patterns, gradient orbs

## 3. Layout & Structure

### Page Flow
1. **Sticky Header** - Transparent → solid on scroll
2. **Hero** - Full viewport height, gradient background, floating phone mockup
3. **Categories** - Horizontal scroll pills with icons
4. **Featured Products** - 4-column grid (desktop), 2-column (tablet), 1-column (mobile)
5. **Promotions Banner** - Full-width gradient with countdown
6. **Benefits** - 4-column icon grid
7. **Testimonials** - Carousel/slider
8. **FAQ** - Accordion style
9. **Contact** - Split layout: form + info
10. **Footer** - Multi-column links + social

### Responsive Breakpoints
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

## 4. Features & Interactions

### Navigation
- Logo click → scroll to top
- Menu items → smooth scroll to sections
- Cart icon → slide-out cart panel (right side)
- Mobile: hamburger → full-screen overlay menu
- "Comprar ahora" button → scroll to products

### Product Cards
- **Default:** Image, name, price, add-to-cart button
- **Hover:** Lift effect, quick-view button appears
- **Click "Agregar al carrito":** 
  - Button changes to checkmark briefly
  - Cart count updates with bounce animation
  - Toast notification "Producto agregado"
- **Discount badge:** Top-right corner, percentage

### Cart Panel
- Slides in from right (400px width desktop, full-width mobile)
- Backdrop blur overlay
- Product list with:
  - Thumbnail
  - Name
  - Unit price
  - Quantity +/- buttons
  - Remove button
  - Line total
- Sticky footer with:
  - Subtotal
  - "Finalizar compra" button
- Empty state: illustration + "Tu carrito está vacío"
- Persists in localStorage

### Category Filters
- Pills with icons
- Active state: filled background
- Click → filter products with fade animation
- "Todos" option to reset

### Countdown Timer
- Days, hours, minutes, seconds
- Updates every second
- Expired state: "¡Oferta terminada!"

### FAQ Accordion
- Click question → expand/collapse answer
- Smooth height animation
- Plus/minus icon rotation
- Only one open at a time

### Contact Form
- Fields: Nombre, Email, Teléfono, Mensaje
- Validation: Required fields, email format
- Submit → success message (no backend)
- WhatsApp button: Opens wa.me link

## 5. Component Inventory

### Header
- **States:** Transparent (top), Solid (scrolled)
- **Elements:** Logo, nav links, cart icon with badge, CTA button
- **Mobile:** Hamburger menu, same elements in overlay

### Product Card
- **States:** Default, Hover (lifted), Loading (skeleton)
- **Elements:** Image, discount badge, brand tag, name, specs pills, price (current + old), CTA button
- **Specs shown:** Almacenamiento, RAM, Cámara, Batería

### Cart Item
- **States:** Default, Quantity updating, Removing (fade out)
- **Elements:** Thumbnail, name, unit price, quantity controls, line total, remove button

### Button Primary
- **States:** Default (#2563EB), Hover (darken 10%), Active (darken 15%), Disabled (gray)
- **Style:** Rounded-lg, padding 12px 24px, font-semibold

### Button Secondary
- **States:** Default (outline), Hover (filled)
- **Style:** Border-2, transparent bg, border-color primary

### Toast Notification
- **Animation:** Slide up from bottom, auto-dismiss 3s
- **Style:** Rounded, shadow-lg, icon + message

### FAQ Item
- **States:** Collapsed, Expanded
- **Animation:** Height transition 300ms, icon rotation

## 6. Technical Approach

### Stack
- Single HTML file with embedded CSS and JavaScript
- Vanilla JS (no frameworks)
- CSS custom properties for theming
- localStorage for cart persistence

### Architecture
```
HTML Structure:
├── header (sticky)
├── main
│   ├── section#hero
│   ├── section#categorias
│   ├── section#productos
│   ├── section#promociones
│   ├── section#beneficios
│   ├── section#testimonios
│   ├── section#faq
│   ├── section#contacto
├── footer
├── div#cart-panel
├── div#toast-container
```

### JavaScript Modules (inline)
- `cartManager` - Add/remove/update items, localStorage sync
- `uiController` - DOM updates, animations, scroll effects
- `filterManager` - Category filtering logic
- `countdownTimer` - Promotion countdown

### Data Model
```javascript
Product {
  id: string,
  name: string,
  brand: string,
  price: number,
  oldPrice?: number,
  image: string,
  specs: {
    storage: string,
    ram: string,
    camera: string,
    battery: string
  },
  category: 'alta' | 'media' | 'economica'
}

CartItem {
  productId: string,
  quantity: number
}
```

### Products (8 phones)
1. Samsung Galaxy S24 Ultra - $4.299.900 - Gama Alta
2. iPhone 15 Pro - $3.899.900 - Gama Alta
3. Samsung Galaxy A55 - $1.899.900 - Gama Media
4. Xiaomi Redmi Note 13 Pro - $1.399.900 - Gama Media
5. Motorola Edge 50 - $1.799.900 - Gama Media
6. Honor X8b - $1.199.900 - Gama Media
7. Samsung Galaxy A15 - $899.900 - Gama Económica
8. Xiaomi Redmi 13C - $649.900 - Gama Económica

## 7. Content

### Hero
- **Title:** "Los Mejores Celulares al Mejor Precio en Colombia"
- **Subtitle:** "Encuentra smartphones de gama alta, media y económica con promociones exclusivas, pago seguro y envío rápido a todo el país."

### Promotions
- "¡30% OFF en toda la línea Samsung!"
- "Envío GRATIS a toda Colombia"
- "12 cuotas sin interés"
- Countdown: 3 días, 12 horas, 45 minutos

### Trust Badges
- Pago 100% Seguro
- Envíos Rapidos a Todo Colombia
- Garantia de 12 Meses
- Productos 100% Originales
- Soporte por WhatsApp

### FAQs
1. ¿Los celulares son nuevos y originales? - Sí, todos nuestros productos son 100% nuevos y originales con garantía oficial.
2. ¿Hacen envíos a toda Colombia? - Sí, enviamos a todas las ciudades con cobertura de 2-5 días hábiles.
3. ¿Qué métodos de pago aceptan? - Tarjeta de crédito/débito, PSE, Nequi, Daviplata, transferencia bancaria.
4. ¿Los equipos tienen garantía? - Todos incluyen 12 meses de garantía oficial del fabricante.
5. ¿Puedo pagar a cuotas? - Sí, hasta 12 cuotas sin interés con tarjetas participantes.
6. ¿Cuánto tarda el envío? - 2-5 días hábiles según tu ciudad.

### Testimonials
1. "Excelente servicio, mi Samsung llegó en perfecto estado y rápido." - Laura M., Bogotá
2. "Los mejores precios que encontré, además el soporte por WhatsApp es muy bueno." - Carlos R., Medellín
3. "Compré el iPhone 15 y estoy encantado, totalmente recomendado." - Andrea V., Cali
4. "Muy fácil comprar, el carrito funciona perfecto y el pago fue sécurisé." - Juan P., Barranquilla
