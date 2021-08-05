from django.db import models

from state_data.models import (
    LGA,
    States, 
    Ward,
    Party
)

from django.contrib.auth import get_user_model
Voters = get_user_model()


class ANNOUNCED_LGA_RESULTS(models.Model):
    lga_name = models.ForeignKey(LGA, on_delete=models.CASCADE)
    party_abbreviation = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    party_score  = models.PositiveIntegerField()
    entered_by_user = models.ForeignKey(Voters, on_delete=models.SET_NULL, null=True)
    date_entered  = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=60, verbose_name="User's IP-address")

    def __str__(self) -> str:
        return f"{self.lga_name} {self.party_score}"

    class Meta:
        verbose_name = "Anounced LGA Results"
        verbose_name_plural = "Anounced LGA Results"


class ANNOUNCED_PU_RESULTS(models.Model):
    lga_name = models.ForeignKey(LGA,on_delete=models.SET_NULL, null=True)
    party_abbreviation = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    party_score  = models.PositiveIntegerField()
    entered_by_user = models.ForeignKey(Voters, on_delete=models.SET_NULL, null=True)
    date_entered  = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=60, verbose_name="User's IP-address")


    def __str__(self) -> str:
        return f"{self.lga_name}: {self.party_abbreviation} - {self.party_score}"

    class Meta:
        verbose_name = "Anounced PU Results"
        verbose_name_plural = "Anounced PU Results"


class ANNOUNCED_WARD_RESULTS(models.Model):
    ward_name = models.ForeignKey(Ward, on_delete=models.CASCADE)
    party_abbreviation = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    party_score  = models.PositiveIntegerField()
    entered_by_user = models.ForeignKey(Voters, on_delete=models.SET_NULL, null=True)
    date_entered  = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=60, verbose_name="User's IP-address")


    def __str__(self) -> str:
        return f"{self.party_abbreviation} - {self.party_score}"

    class Meta:
        verbose_name = "Anounced Ward Results"
        verbose_name_plural = "Anounced Ward Results"


class ANNOUNCED_STATE_RESULTS(models.Model):
    state_name = models.ForeignKey(States, on_delete=models.CASCADE)
    party_abbreviation = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    party_score  = models.PositiveIntegerField()
    entered_by_user = models.ForeignKey(Voters, null=True, on_delete=models.SET_NULL)
    date_entered = models.DateTimeField(auto_now_add=True,)
    user_ip_address = models.CharField(max_length=60, verbose_name="User's IP-address")


    def __str__(self) -> str:
        return f"{self.party_abbreviation} - {self.party_score}"

    class Meta:
        verbose_name = "Anounced State Results"
        verbose_name_plural = "Anounced State Results"
