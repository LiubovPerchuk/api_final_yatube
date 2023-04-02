from rest_framework import filters, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .permissions import AuthorOrReadOnly
from .serializers import (
    CommentSerializer, GroupSerializer, FollowSerializer, PostSerializer)
from posts.models import Group, Post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Endpoint для получения группы."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    """Endpoint для получения, создания, изменения и удаления постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, AuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Метод вызова сериализатора для создания и сохранения поста."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Endpoint для получения, создания, изменения и удаления комментариев."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, AuthorOrReadOnly]

    def get_queryset(self):
        """Метод возвращения всех комментариев к посту."""
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments.all()

    def perform_create(self, serializer):
        """Метод вызова сериализатора для создания
        и сохранения комментария к посту."""
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Endpoint для получения, создания, изменения и удаления подписок."""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, AuthorOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username", )

    def get_queryset(self):
        """Метод возвращения подписки на автора."""
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        """Метод вызова сериализатора для создания
        подписки на автора."""
        serializer.save(user=self.request.user)
