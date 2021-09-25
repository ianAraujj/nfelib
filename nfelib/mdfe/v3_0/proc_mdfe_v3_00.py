from dataclasses import dataclass, field
from typing import Optional
from nfelib.mdfe.v3_0.mdfe_tipos_basico_v3_00 import (
    Tmdfe,
    TprotMdfe,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class MdfeProc:
    """
    MDF-e processado.

    :ivar mdfe:
    :ivar prot_mdfe:
    :ivar versao:
    :ivar ip_transmissor: IP do transmissor do documento fiscal para o
        ambiente autorizador
    :ivar n_porta_con: Porta de origem utilizada na conexão (De 0 a
        65535)
    :ivar dh_conexao: Data e Hora da Conexão de Origem
    """
    class Meta:
        name = "mdfeProc"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    mdfe: Optional[Tmdfe] = field(
        default=None,
        metadata={
            "name": "MDFe",
            "type": "Element",
            "required": True,
        }
    )
    prot_mdfe: Optional[TprotMdfe] = field(
        default=None,
        metadata={
            "name": "protMDFe",
            "type": "Element",
            "required": True,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"3\.00",
        }
    )
    ip_transmissor: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipTransmissor",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
        }
    )
    n_porta_con: Optional[str] = field(
        default=None,
        metadata={
            "name": "nPortaCon",
            "type": "Attribute",
            "pattern": r"[0-9]{1,5}",
        }
    )
    dh_conexao: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhConexao",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
