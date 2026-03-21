#!/usr/bin/env python3
"""
LEGAL_AGENT - Generador de documentos legales
"""
import json
from pathlib import Path

BASE = Path.home() / "AutonomousSystem"

class LegalAgent:
    def generate_contract(self, contract_type):
        """Genera contrato básico"""
        
        contracts = {
            "servicios": self.contract_servicios(),
            "privacidad": self.contract_privacidad(),
            "terminos": self.contract_terminos(),
            "nda": self.contract_nda()
        }
        
        return contracts.get(contract_type, "Tipo no disponible")
    
    def contract_servicios(self):
        return """# CONTRATO DE SERVICIOS

**AVISO LEGAL: Este documento es una plantilla básica y DEBE ser revisado por un abogado local antes de su uso.**

---

## PARTES
**Proveedor:** [Nombre de tu empresa]
**Cliente:** [Nombre del cliente]

## SERVICIOS
[Descripción detallada de los servicios a prestar]

## PAGO
- Monto: $[MONTO]
- Forma de pago: [mensual/único]
- Método: [transferencia/PayPal/etc]

## PLAZO
Duración: [fecha inicio] a [fecha fin]

## RESPONSABILIDADES
- El proveedor se compromete a...
- El cliente se compromete a...

## TERMINACIÓN
Cualquier parte puede terminar con [30] días de aviso previo.

## LIMITACIÓN DE RESPONSABILIDAD
[Según leyes locales]

---

**NOTA:** Este documento es solo una guía. Consulta un abogado."""

    def contract_privacidad(self):
        return """# POLÍTICA DE PRIVACIDAD

**Fecha de vigencia:** [FECHA]

## DATOS QUE RECOLECTAMOS
- Información de contacto (nombre, email, teléfono)
- Datos de uso de la aplicación
- Cookies y tecnologías similares

## USO DE DATOS
- Proveer nuestros servicios
- Mejorar experiencia de usuario
- Comunicarnos contigo

## PROTECCIÓN
Implementamos medidas de seguridad apropiadas...

## TUS DERECHOS
- Acceso a tus datos
- Rectificación
- Eliminación
- Portabilidad

---

**CONTACTO:** [email@tuempresa.com]

**AVISO:** Esta política es una plantilla básica."""

    def contract_terminos(self):
        return """# TÉRMINOS Y CONDICIONES

**Última actualización:** [FECHA]

## USO DEL SERVICIO
Al usar este servicio aceptas estos términos.

## CUENTAS DE USUARIO
- Eres responsable de tu cuenta
- Debes mantener tu contraseña segura

## PROHIBICIONES
No puedes:
- Usar para fines ilegales
- Interferir con el servicio
- Intentar acceder a cuentas de otros

## PROPIEDAD INTELECTUAL
Todo el contenido es propiedad de [Tu Empresa]

## CAMBIOS
Podemos modificar estos términos.

---

**CONTACTO:** [email@tuempresa.com]"""

    def contract_nda(self):
        return """# ACUERDO DE CONFIDENCIALIDAD (NDA)

**PARTES:**
- Parte Reveladora: [Nombre]
- Parte Receptora: [Nombre]

**OBJETO:** [Descripción de la información confidencial]

## INFORMACIÓN CONFIDENCIAL
[Definir qué se considera información confidencial]

## OBLIGACIONES
La Parte Receptora se compromete a:
- No revelar a terceros
- Usar solo para el propósito acordado
- Mantener seguridad adecuada

## EXCEPCIONES
No aplica a información que:
- Era pública antes
- Se obtiene de terceros
- Se desarrolla independientemente

## DURACIÓN
Este acuerdo dura [2-5] años.

---

**⚠️ IMPORTANTE:** Debe ser revisado por abogado local."""

    def run(self, contract_type="servicios"):
        print("⚖️ LEGAL AGENT - Generando documento...\n")
        
        contract = self.generate_contract(contract_type)
        
        # Guardar
        output = BASE / "data" / f"{contract_type}_contract.md"
        output.write_text(contract)
        
        print(f"✅ Contrato generado: {output}")
        print("\n" + "="*50)
        print(contract[:500] + "...")
        
        return f"Contrato {contract_type} generado"

if __name__ == "__main__":
    import sys
    ctype = sys.argv[1] if len(sys.argv) > 1 else "servicios"
    LegalAgent().run(ctype)
