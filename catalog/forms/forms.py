from django import forms
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

from catalog.models import Product

from .mixins import StyleFormMixin


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    message = forms.CharField(widget=forms.Textarea, label="Ваше сообщение")


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    # Список запрещённых слов
    FORBIDDEN_WORDS = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Добавляем класс CSS к каждому полю
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        # Можно добавить placeholder к полям, если это необходимо
        self.fields["name"].widget.attrs[
            "placeholder"
        ] = "Введите наименование продукта"
        self.fields["description"].widget.attrs[
            "placeholder"
        ] = "Введите описание продукта"
        self.fields["price"].widget.attrs["placeholder"] = "Введите цену продукта"

    def clean_name(self):
        name = self.cleaned_data["name"]
        self.check_forbidden_words(name, "Наименование продукта")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        self.check_forbidden_words(description, "Описание")
        return description

    def check_forbidden_words(self, text, field_name):
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in text.lower():
                raise forms.ValidationError(
                    f"Поле '{field_name}' содержит запрещённое слово: '{word}'"
                )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Цена продукта не может быть отрицательной.")
        return price

    def clean_image(self):
        """
        Валидация для загрузки изображения: проверка формата и размера файла.
        """
        image = self.cleaned_data.get("image")

        # Проверка на пустое поле (если изображение не загружено)
        if image:
            # Проверка формата изображения
            if not image.name.endswith(("jpg", "jpeg", "png")):
                raise ValidationError(
                    "Файл изображения должен быть в формате JPEG или PNG."
                )

            # Проверка размера файла
            if image.size > 5 * 1024 * 1024:  # 5 MB
                raise ValidationError("Размер изображения не должен превышать 5 МБ.")

            # Проверка на корректность изображения
            try:
                width, height = get_image_dimensions(image)
                if width < 100 or height < 100:
                    raise ValidationError(
                        "Минимальные размеры изображения: 100x100 пикселей."
                    )
            except Exception:
                raise ValidationError("Ошибка при обработке изображения.")
        return image
