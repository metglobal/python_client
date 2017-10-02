# hotelspro_client.DefaultApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availability_product_code_get**](DefaultApi.md#availability_product_code_get) | **GET** /availability/{product_code} | Availability with Product Code
[**book_provision_code_post**](DefaultApi.md#book_provision_code_post) | **POST** /book/{provision_code} | Book with Provision Code
[**bookings_booking_code_get**](DefaultApi.md#bookings_booking_code_get) | **GET** /bookings/{booking_code} | Get Booking Detail
[**bookings_get**](DefaultApi.md#bookings_get) | **GET** /bookings/ | Get Booking List
[**cancel_booking_code_post**](DefaultApi.md#cancel_booking_code_post) | **POST** /cancel/{booking_code} | Cancel Booking with Booking Code
[**hotel_availability_get**](DefaultApi.md#hotel_availability_get) | **GET** /hotel-availability/ | Hotel Availability with Hotel Code and Search Code
[**provision_product_code_post**](DefaultApi.md#provision_product_code_post) | **POST** /provision/{product_code} | Provision with Product Code
[**search_post**](DefaultApi.md#search_post) | **POST** /search/ | Search with Hotel Code(Hotel Code List) or Destination Code or Geolocation


# **availability_product_code_get**
> AvailabilityResponse availability_product_code_get(product_code)

Availability with Product Code

Check Availability of Selected Product

### Example 
```python
from __future__ import print_function
import time
import hotelspro_client
from hotelspro_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
hotelspro_client.configuration.username = 'YOUR_USERNAME'
hotelspro_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hotelspro_client.DefaultApi()
product_code = 'product_code_example' # str | product code that returned in Search(or Hotel Availability) Response

try: 
    # Availability with Product Code
    api_response = api_instance.availability_product_code_get(product_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->availability_product_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**| product code that returned in Search(or Hotel Availability) Response | 

### Return type

[**AvailabilityResponse**](AvailabilityResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **book_provision_code_post**
> BookResponse book_provision_code_post(name, provision_code)

Book with Provision Code

Returns Book Response

### Example 
```python
from __future__ import print_function
import time
import hotelspro_client
from hotelspro_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
hotelspro_client.configuration.username = 'YOUR_USERNAME'
hotelspro_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hotelspro_client.DefaultApi()
name = ['name_example'] # list[str] | A person's name.
provision_code = 'provision_code_example' # str | 

try: 
    # Book with Provision Code
    api_response = api_instance.book_provision_code_post(name, provision_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->book_provision_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**list[str]**](str.md)| A person&#39;s name. | 
 **provision_code** | **str**|  | 

### Return type

[**BookResponse**](BookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bookings_booking_code_get**
> BookResponse bookings_booking_code_get(booking_code)

Get Booking Detail

Returns past booking(s) data.

### Example 
```python
from __future__ import print_function
import time
import hotelspro_client
from hotelspro_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
hotelspro_client.configuration.username = 'YOUR_USERNAME'
hotelspro_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hotelspro_client.DefaultApi()
booking_code = 'booking_code_example' # str | This is the code that taken from the response of bookings request

try: 
    # Get Booking Detail
    api_response = api_instance.bookings_booking_code_get(booking_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bookings_booking_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_code** | **str**| This is the code that taken from the response of bookings request | 

### Return type

[**BookResponse**](BookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bookings_get**
> BookingListResponse bookings_get(from_date=from_date, to_date=to_date, format=format)

Get Booking List

Returns past booking(s) data.

### Example 
```python
from __future__ import print_function
import time
import hotelspro_client
from hotelspro_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
hotelspro_client.configuration.username = 'YOUR_USERNAME'
hotelspro_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hotelspro_client.DefaultApi()
from_date = 'from_date_example' # str | This is the booking date for filtering the bookings from the from_date(YYYY-MM-DD). (optional)
to_date = 'to_date_example' # str | This is the booking date for filtering the bookings until the to_date(YYYY-MM-DD). (optional)
format = 'format_example' # str | Only JSON supported (optional)

try: 
    # Get Booking List
    api_response = api_instance.bookings_get(from_date=from_date, to_date=to_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bookings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **str**| This is the booking date for filtering the bookings from the from_date(YYYY-MM-DD). | [optional] 
 **to_date** | **str**| This is the booking date for filtering the bookings until the to_date(YYYY-MM-DD). | [optional] 
 **format** | **str**| Only JSON supported | [optional] 

### Return type

[**BookingListResponse**](BookingListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_booking_code_post**
> CancelResponse cancel_booking_code_post(booking_code)

Cancel Booking with Booking Code

Cancel the Booking

### Example 
```python
from __future__ import print_function
import time
import hotelspro_client
from hotelspro_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
hotelspro_client.configuration.username = 'YOUR_USERNAME'
hotelspro_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hotelspro_client.DefaultApi()
booking_code = 'booking_code_example' # str | Booking Code that returned in Book Response

try: 
    # Cancel Booking with Booking Code
    api_response = api_instance.cancel_booking_code_post(booking_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_booking_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_code** | **str**| Booking Code that returned in Book Response | 

### Return type

[**CancelResponse**](CancelResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotel_availability_get**
> HotelAvailabilityResponse hotel_availability_get(search_code, hotel_code)

Hotel Availability with Hotel Code and Search Code

Check Availability of Selected Hotel

### Example 
```python
from __future__ import print_function
import time
import hotelspro_client
from hotelspro_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
hotelspro_client.configuration.username = 'YOUR_USERNAME'
hotelspro_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hotelspro_client.DefaultApi()
search_code = 'search_code_example' # str | search code that returned in search response
hotel_code = 'hotel_code_example' # str | requested hotel code

try: 
    # Hotel Availability with Hotel Code and Search Code
    api_response = api_instance.hotel_availability_get(search_code, hotel_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hotel_availability_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_code** | **str**| search code that returned in search response | 
 **hotel_code** | **str**| requested hotel code | 

### Return type

[**HotelAvailabilityResponse**](HotelAvailabilityResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_product_code_post**
> ProvisionResponse provision_product_code_post(product_code)

Provision with Product Code

Provision of Selected Product

### Example 
```python
from __future__ import print_function
import time
import hotelspro_client
from hotelspro_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
hotelspro_client.configuration.username = 'YOUR_USERNAME'
hotelspro_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hotelspro_client.DefaultApi()
product_code = 'product_code_example' # str | product code that returned in Search(or Hotel Availability) Response

try: 
    # Provision with Product Code
    api_response = api_instance.provision_product_code_post(product_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->provision_product_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**| product code that returned in Search(or Hotel Availability) Response | 

### Return type

[**ProvisionResponse**](ProvisionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_post**
> SearchResponse search_post(pax, checkin, checkout, client_nationality, currency, hotel_code=hotel_code, destination_code=destination_code, lat=lat, lon=lon, radius=radius, max_product=max_product)

Search with Hotel Code(Hotel Code List) or Destination Code or Geolocation

Returns list of products

### Example 
```python
from __future__ import print_function
import time
import hotelspro_client
from hotelspro_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
hotelspro_client.configuration.username = 'YOUR_USERNAME'
hotelspro_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hotelspro_client.DefaultApi()
pax = ['pax_example'] # list[str] | Number of pax
checkin = 'checkin_example' # str | Checkin
checkout = 'checkout_example' # str | Checkout
client_nationality = 'client_nationality_example' # str | Client Nationality
currency = 'currency_example' # str | Currency (Supported Currencies USD, EUR, GBP, TRY)
hotel_code = 'hotel_code_example' # str | Requested Hotel Code (optional)
destination_code = 'destination_code_example' # str | Requested Destination Code (optional)
lat = 'lat_example' # str | Requested Latitude Code(lat, lon and radius should be given together) (optional)
lon = 'lon_example' # str | Requested Longitude Code(lat, lon and radius should be given together) (optional)
radius = 'radius_example' # str | Requested Radius Code(lat, lon and radius should be given together) (optional)
max_product = 56 # int | Max Product (optional)

try: 
    # Search with Hotel Code(Hotel Code List) or Destination Code or Geolocation
    api_response = api_instance.search_post(pax, checkin, checkout, client_nationality, currency, hotel_code=hotel_code, destination_code=destination_code, lat=lat, lon=lon, radius=radius, max_product=max_product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pax** | [**list[str]**](str.md)| Number of pax | 
 **checkin** | **str**| Checkin | 
 **checkout** | **str**| Checkout | 
 **client_nationality** | **str**| Client Nationality | 
 **currency** | **str**| Currency (Supported Currencies USD, EUR, GBP, TRY) | 
 **hotel_code** | **str**| Requested Hotel Code | [optional] 
 **destination_code** | **str**| Requested Destination Code | [optional] 
 **lat** | **str**| Requested Latitude Code(lat, lon and radius should be given together) | [optional] 
 **lon** | **str**| Requested Longitude Code(lat, lon and radius should be given together) | [optional] 
 **radius** | **str**| Requested Radius Code(lat, lon and radius should be given together) | [optional] 
 **max_product** | **int**| Max Product | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

