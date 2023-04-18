# encoding: utf-8
# module IdeaRS.OpenModel.Message calls itself Message
# from IdeaRS.OpenModel, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class OpenMessage(OpenObject):
    """ OpenMessage() """
    @staticmethod
    def Create(number, openObject, propertyName, description, innerMessage):
        """ Create(number: MessageNumber, openObject: OpenObject, propertyName: str, description: str, innerMessage: OpenMessage) -> OpenMessage """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: OpenMessage) -> str

Set: Description(self: OpenMessage) = value
"""

    InnerMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerMessage(self: OpenMessage) -> OpenMessage

Set: InnerMessage(self: OpenMessage) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: OpenMessage) -> str

"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: OpenMessage) -> MessageNumber

Set: Number(self: OpenMessage) = value
"""

    Object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object(self: OpenMessage) -> OpenObject

Set: Object(self: OpenMessage) = value
"""

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyName(self: OpenMessage) -> str

Set: PropertyName(self: OpenMessage) = value
"""

    PropertyValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyValue(self: OpenMessage) -> object

"""



class ErrorMessage(OpenMessage):
    """ ErrorMessage() """
    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: ErrorMessage) -> str

"""



class IDEAProgress(object):
    """ IDEAProgress(callback: Action[IDEAProgressReport]) """
    def Report(self, data):
        """ Report(self: IDEAProgress, data: IDEAProgressReport) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, callback):
        """ __new__(cls: type, callback: Action[IDEAProgressReport]) """
        pass


class IDEAProgressReport(object):
    """ IDEAProgressReport() """
    CurrentProgressAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentProgressAmount(self: IDEAProgressReport) -> int

Set: CurrentProgressAmount(self: IDEAProgressReport) = value
"""

    CurrentProgressMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentProgressMessage(self: IDEAProgressReport) -> str

Set: CurrentProgressMessage(self: IDEAProgressReport) = value
"""

    TotalProgressAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalProgressAmount(self: IDEAProgressReport) -> int

Set: TotalProgressAmount(self: IDEAProgressReport) = value
"""



class IIOMSettings:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryCode(self: IIOMSettings) -> CountryCode

Set: CountryCode(self: IIOMSettings) = value
"""

    CreatedSuccessfully = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedSuccessfully(self: IIOMSettings) -> bool

Set: CreatedSuccessfully(self: IIOMSettings) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: IIOMSettings) -> str

Set: FileName(self: IIOMSettings) = value
"""



class InformationMessage(OpenMessage):
    """ InformationMessage() """
    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: InformationMessage) -> str

"""



class IOMSettings(object, IIOMSettings):
    """ IOMSettings() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryCode(self: IOMSettings) -> CountryCode

Set: CountryCode(self: IOMSettings) = value
"""

    CreatedSuccessfully = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedSuccessfully(self: IOMSettings) -> bool

Set: CreatedSuccessfully(self: IOMSettings) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: IOMSettings) -> str

Set: FileName(self: IOMSettings) = value
"""



class MessageNumber(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) MessageNumber, values: ErrBadWeldMaterialProperty (67108887), ErrBoltsTooClose (67108871), ErrBoltsTooCloseEdge (67108872), ErrContactsAngle (67108873), ErrCurveDecreaseFunction (67108880), ErrCurveDerivation (67108881), ErrCurveFunction (67108879), ErrCurveNotSet (67108882), ErrCurveZeroPoint (67108878), ErrDataObjectNotCreated (67108866), ErrIncorrectMaterialEGP (67108875), ErrIncorrentMaterialE (67108874), ErrNoCrossSectionParameter (67108870), ErrNoEquivalentObjectInDataModel (67108869), ErrNoInLibrary (67108886), ErrNoObjectInOpenModel (67108867), ErrNoOpenObject (67108865), ErrNoReferenceObjectInOpenModel (67108868), Error (67108864), ErrPreloadedBoltGrade (67108876), ErrTimeout (67108885), ErrValidPolyline (67108883), ErrValueOutOfRange (67108877), ErrWarningLoad (67108884), Information (16777216), Reserved (134217728), Unspecified (0), WarnCurveCount (33554435), Warning (33554432), WarnNoPropertyInData (33554433), WarnReinforcementBarsCollision (33554437), WarnValueOutOfRange (33554434) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ErrBadWeldMaterialProperty = None
    ErrBoltsTooClose = None
    ErrBoltsTooCloseEdge = None
    ErrContactsAngle = None
    ErrCurveDecreaseFunction = None
    ErrCurveDerivation = None
    ErrCurveFunction = None
    ErrCurveNotSet = None
    ErrCurveZeroPoint = None
    ErrDataObjectNotCreated = None
    ErrIncorrectMaterialEGP = None
    ErrIncorrentMaterialE = None
    ErrNoCrossSectionParameter = None
    ErrNoEquivalentObjectInDataModel = None
    ErrNoInLibrary = None
    ErrNoObjectInOpenModel = None
    ErrNoOpenObject = None
    ErrNoReferenceObjectInOpenModel = None
    Error = None
    ErrPreloadedBoltGrade = None
    ErrTimeout = None
    ErrValidPolyline = None
    ErrValueOutOfRange = None
    ErrWarningLoad = None
    Information = None
    Reserved = None
    Unspecified = None
    value__ = None
    WarnCurveCount = None
    Warning = None
    WarnNoPropertyInData = None
    WarnReinforcementBarsCollision = None
    WarnValueOutOfRange = None


class NonConformity(object):
    """ NonConformity() """
    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Guid(self: NonConformity) -> Guid

Set: Guid(self: NonConformity) = value
"""

    Severity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Severity(self: NonConformity) -> NonConformitySeverity

Set: Severity(self: NonConformity) = value
"""



class NonConformityIssue(object):
    """ NonConformityIssue() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: NonConformityIssue) -> str

Set: Description(self: NonConformityIssue) = value
"""

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Guid(self: NonConformityIssue) -> Guid

Set: Guid(self: NonConformityIssue) = value
"""

    Severity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Severity(self: NonConformityIssue) -> NonConformitySeverity

Set: Severity(self: NonConformityIssue) = value
"""



class NonConformitySeverity(Enum, IComparable, IFormattable, IConvertible):
    """ enum NonConformitySeverity, values: Error (2), Info (0), TerminatedError (3), Warning (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Error = None
    Info = None
    TerminatedError = None
    value__ = None
    Warning = None


class OpenMessages(object):
    """ OpenMessages() """
    def Add(self, message):
        """ Add(self: OpenMessages, message: OpenMessage) """
        pass

    def Remove(self, message):
        """ Remove(self: OpenMessages, message: OpenMessage) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    ErrorMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorMessages(self: OpenMessages) -> List[ErrorMessage]

"""

    InformationMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InformationMessages(self: OpenMessages) -> List[InformationMessage]

"""

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Messages(self: OpenMessages) -> List[OpenMessage]

Set: Messages(self: OpenMessages) = value
"""

    WarningMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarningMessages(self: OpenMessages) -> List[WarningMessage]

"""



class WarningMessage(OpenMessage):
    """
    WarningMessage()
    WarningMessage(number: MessageNumber, openObject: OpenObject, propertyName: str, description: str, innerMessage: OpenMessage)
    """
    @staticmethod # known case of __new__
    def __new__(self, number=None, openObject=None, propertyName=None, description=None, innerMessage=None):
        """
        __new__(cls: type)
        __new__(cls: type, number: MessageNumber, openObject: OpenObject, propertyName: str, description: str, innerMessage: OpenMessage)
        """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: WarningMessage) -> str

"""



