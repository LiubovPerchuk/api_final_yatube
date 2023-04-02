from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        model = Group
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username")

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("author", "post")


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""
    user = serializers.SlugRelatedField(
        read_only=True, slug_field="username",
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all())

    class Meta:
        fields = "__all__"
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following")
            )
        ]

    def validate_following(self, following):
        """Метод подтверждения подписки."""
        if self.context.get("request").user == following:
            raise serializers.ValidationError(
                "Вы не можете подписаться на себя.")
        return following
