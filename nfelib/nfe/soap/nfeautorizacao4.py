from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteZipInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfe_dados_msg_zip: Optional[str] = field(
            default=None,
            metadata={
                "name": "nfeDadosMsgZip",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            }
        )


@dataclass
class NfeDadosMsg:
    class Meta:
        name = "nfeDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class NfeDadosMsgZip:
    class Meta:
        name = "nfeDadosMsgZip"
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class NfeMonitoria:
    class Meta:
        name = "nfeMonitoria"
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"

    nome_servidor: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeServidor",
            "type": "Element",
        }
    )
    dh_servidor: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhServidor",
            "type": "Element",
        }
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class NfeResultMsg:
    class Meta:
        name = "nfeResultMsg"
        nillable = True
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )
    header: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
                "nillable": True,
            }
        )
        fault: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput.Body.Fault"] = field(
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

    @dataclass
    class Header:
        nfe_monitoria: Optional[NfeMonitoria] = field(
            default=None,
            metadata={
                "name": "nfeMonitoria",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            }
        )


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteInput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            }
        )


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )
    header: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteOutput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
                "nillable": True,
            }
        )
        fault: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteOutput.Body.Fault"] = field(
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

    @dataclass
    class Header:
        nfe_monitoria: Optional[NfeMonitoria] = field(
            default=None,
            metadata={
                "name": "nfeMonitoria",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            }
        )


class NfeAutorizacao4SoapNfeAutorizacaoLote:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4/nfeAutorizacaoLote"
    input = NfeAutorizacao4SoapNfeAutorizacaoLoteInput
    output = NfeAutorizacao4SoapNfeAutorizacaoLoteOutput


class NfeAutorizacao4SoapNfeAutorizacaoLoteZip:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4/nfeAutorizacaoLoteZip"
    input = NfeAutorizacao4SoapNfeAutorizacaoLoteZipInput
    output = NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput
