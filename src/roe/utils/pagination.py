"""Pagination utilities."""

from urllib.parse import parse_qs, urlparse


class PaginationHelper:
    """Helper for handling paginated responses."""

    @staticmethod
    def extract_page_from_url(url: str | None) -> int | None:
        """Extract page number from a pagination URL.

        Args:
            url: Pagination URL (e.g., from next/previous links).

        Returns:
            Page number if found, None otherwise.
        """
        if not url:
            return None

        try:
            parsed = urlparse(url)
            query_params = parse_qs(parsed.query)

            if "page" in query_params:
                return int(query_params["page"][0])
        except (ValueError, IndexError, KeyError):
            pass

        return None

    @staticmethod
    def build_query_params(
        organization_id: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs,
    ) -> dict[str, str]:
        """Build query parameters for paginated requests.

        Args:
            organization_id: Organization ID (always required).
            page: Page number (optional).
            page_size: Page size (optional).
            **kwargs: Additional query parameters.

        Returns:
            Dictionary of query parameters.
        """
        params = {"organization_id": organization_id}

        if page is not None:
            params["page"] = str(page)

        if page_size is not None:
            params["page_size"] = str(page_size)

        # Add any additional parameters
        for key, value in kwargs.items():
            if value is not None:
                params[key] = str(value)

        return params
