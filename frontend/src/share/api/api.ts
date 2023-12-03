import axios, { type AxiosInstance } from 'axios'
import Cookies from 'js-cookie'
import { TOKEN_COOKIES } from 'share/const/localstorage'

const BaseURL = '45.147.248.21:8000/api/'

export class API {
    constructor () {
        this.apiInstance = axios.create(({
            baseURL: BaseURL,
            headers: {
                Authorization: Cookies.get(TOKEN_COOKIES)?  `Token ${Cookies.get(TOKEN_COOKIES)}` : ''
            }
        }))
    }

    apiInstance: AxiosInstance
}
