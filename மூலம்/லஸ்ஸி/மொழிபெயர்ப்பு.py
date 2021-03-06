import types

from லஸ்ஸியிலக்கணங்கள் import நிரல்மொழிகள்

from எண்ணிக்கை import உரைக்கு as உ
from ._வெளியே.lark import Token
from ._வெளியே.lark.visitors import Visitor_Recursive
from .பகுப்பாய்வி import பகுப்பாய்வி_பெறு, புனரமைப்பு_பெறு, பின்_புனரமைப்பு_பெறு, வரிசைமாற்றி_பெறு


class எண்ணுரு_மாற்றம்(Visitor_Recursive):
    def __init__(தன், மொழி):
        தன்.மொழி = மொழி

    def number(தன், மரம்):
        assert மரம்.data == "number"
        மரம்.children[0] = Token(மரம்.children[0].type, உ(மரம்.children[0].value, தன்.மொழி))


class இனங்காட்டி_மாற்றம்(Visitor_Recursive):
    def __init__(தன், மொழி, மூல்மொழி, இனங்காட்டி_கிளைகள், இனங்காட்டி_மாற்றங்கள்):
        தன்.மொழி = மொழி
        தன்.மூல்மொழி = மூல்மொழி
        தன்.மாற்றங்கள் = இனங்காட்டி_மாற்றங்கள்

        for கிளை, குழந்தைகள் in இனங்காட்டி_கிளைகள்.items():

            def செயலி_உருவாக்கு(குழந்தைகள்_):
                def செயலி(தன், மரம்):
                    if குழந்தைகள்_ is True:
                        குழந்தை_பட்டியல் = range(len(மரம்.children))
                    elif isinstance(குழந்தைகள்_, list):
                        குழந்தை_பட்டியல் = குழந்தைகள்_
                    else:
                        குழந்தை_பட்டியல் = [குழந்தைகள்_]

                    for கு in குழந்தை_பட்டியல்:
                        மரம்.children[கு] = Token(மரம்.children[கு].type, தன்._மாற்றம்(மரம்.children[கு].value))

                return செயலி

            setattr(தன், கிளை, types.MethodType(செயலி_உருவாக்கு(குழந்தைகள்_=குழந்தைகள்), தன்))

    def _மாற்றம்(தன், உரை):
        try:
            d = next(இ for இ in தன்.மாற்றங்கள் if தன்.மூல்மொழி in இ and இ[தன்.மூல்மொழி] == உரை)
            return d[தன்.மொழி]
        except (StopIteration, KeyError):
            return உரை


def மொழியாக்கம்(உரை, நிரல்மொழி, மொழி, மூல்மொழி=None, எண்ணுரு=None, மூலெண்ணுரு=None, இனங்காட்டிகள்=None, பதிப்பு=None):
    பகுப்பாய்வி = பகுப்பாய்வி_பெறு(நிரல்மொழி, மொழி=மூல்மொழி, எண்ணுரு=மூலெண்ணுரு, பதிப்பு=பதிப்பு)
    எண்ணுரு = நிரல்மொழிகள்.எண்ணுரு_பெறு(நிரல்மொழி, மொழி=மொழி, எண்ணுரு=எண்ணுரு, பதிப்பு=பதிப்பு)
    வரிசை_மாற்றி = வரிசைமாற்றி_பெறு(நிரல்மொழி, மூல்மொழி=மூல்மொழி, வேண்டியமொழி=மொழி, பதிப்பு=பதிப்பு)

    மரம் = பகுப்பாய்வி.parse(உரை)
    if வரிசை_மாற்றி:
        வரிசை_மாற்றி.visit(மரம்)
    எண்ணுரு_மாற்றம்(எண்ணுரு).visit(மரம்)

    இனங்காட்டி_கிளைகள் = நிரல்மொழிகள்.தகவல்(நிரல்மொழி, 'இனங்காட்டி கிளைகள்', பதிப்பு=பதிப்பு)
    if இனங்காட்டி_கிளைகள் and இனங்காட்டிகள்:
        இனங்காட்டி_மாற்றம்(மொழி, மூல்மொழி, இனங்காட்டி_கிளைகள், இனங்காட்டிகள்).visit(மரம்)

    புனரமைப்பு = புனரமைப்பு_பெறு(நிரல்மொழி, மொழி, எண்ணுரு, பதிப்பு=பதிப்பு)
    வெளியீடு = புனரமைப்பு.reconstruct(மரம், postproc=பின்_புனரமைப்பு_பெறு(நிரல்மொழி, பதிப்பு=பதிப்பு))

    return வெளியீடு
