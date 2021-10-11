from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4"


@dataclass
class NfeDadosMsg:
    class Meta:
        name = "nfeDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class NfeResultMsg:
    class Meta:
        name = "nfeResultMsg"
        nillable = True
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class NfeStatusServico4SoapNfeStatusServicoNfInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeStatusServico4SoapNfeStatusServicoNfInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfe_dados_msg: Optional[NfeDadosMsg] = field(
            default=None,
            metadata={
                "name": "nfeDadosMsg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4",
            }
        )


@dataclass
class NfeStatusServico4SoapNfeStatusServicoNfOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeStatusServico4SoapNfeStatusServicoNfOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfe_result_msg: Optional[NfeResultMsg] = field(
            default=None,
            metadata={
                "name": "nfeResultMsg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4",
                "nillable": True,
            }
        )
        fault: Optional["NfeStatusServico4SoapNfeStatusServicoNfOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


class NfeStatusServico4SoapNfeStatusServicoNf:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4/nfeStatusServicoNF"
    input = NfeStatusServico4SoapNfeStatusServicoNfInput
    output = NfeStatusServico4SoapNfeStatusServicoNfOutput
