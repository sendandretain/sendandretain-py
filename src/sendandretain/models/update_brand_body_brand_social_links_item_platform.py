from enum import Enum


class UpdateBrandBodyBrandSocialLinksItemPlatform(str, Enum):
    FACEBOOK = "facebook"
    GITHUB = "github"
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"
    OTHER = "other"
    WEBSITE = "website"
    X = "x"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
