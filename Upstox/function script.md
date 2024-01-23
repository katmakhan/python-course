(()=>{
    "use strict";
    var e, t = {
        265: (e,t,o)=>{
            o.d(t, {
                Z: ()=>a
            });
            var r = o(23645)
              , i = o.n(r)
              , n = o(88029)
              , s = i()((function(e) {
                return e[1]
            }
            ));
            s.i(n.Z),
            s.push([e.id, "html,\nbody,\nmain {\n  height: 100%;\n}\n\niframe[src*='access.upstox.com'] {\n  position: absolute;\n}\n", ""]);
            const a = s
        }
        ,
        98733: (e,t,o)=>{
            o.d(t, {
                Z: ()=>n
            });
            var r = o(23645)
              , i = o.n(r)()((function(e) {
                return e[1]
            }
            ));
            i.push([e.id, ".item-enter {\n  opacity: 0;\n  transform: translateY(40px);\n}\n.item-enter-active {\n  opacity: 1;\n  transform: translateY(0);\n  transition: all 300ms;\n}\n.item-exit {\n  opacity: 1;\n}\n.item-exit-active {\n  opacity: 0;\n  transition: all 300ms;\n}", ""]);
            const n = i
        }
        ,
        33720: (e,t,o)=>{
            o(5097);
            var r = o(67294)
              , i = o(73935)
              , n = o(70798)
              , s = o(22188);
            class a {
                constructor(e) {
                    this.getItem = (e,t=!1)=>{
                        const o = this.storage.getItem(e);
                        return t && o ? JSON.parse(o) : o
                    }
                    ,
                    this.setItem = (e,t)=>{
                        const o = "string" != typeof t ? JSON.stringify(t) : t;
                        this.storage.setItem(e, o)
                    }
                    ,
                    this.removeItem = e=>{
                        this.storage.removeItem(e)
                    }
                    ,
                    this.sync = (e,t)=>{
                        if (void 0 !== t)
                            return null === t ? this.removeItem(e) : void this.setItem(e, t)
                    }
                    ,
                    this.storage = "session" === e ? sessionStorage : localStorage
                }
            }
            const c = new a("session")
              , l = new a("local");
            var u = o(36808)
              , d = o.n(u);
            const p = {
                domain: ".upstox.com",
                path: "/"
            }
              , m = new class {
                constructor() {
                    this.watchers = {
                        access_token: [],
                        refresh_token: [],
                        login_key: [],
                        auth_identity_token: [],
                        auth_identity_token_expiry: [],
                        user_id: [],
                        customer_status: [],
                        lead_phone_number: [],
                        lead_pan_number: [],
                        lead_dob: [],
                        profile_id: [],
                        user_type: [],
                        app_load_start_time: []
                    },
                    this.subscribeCookieChange = (e,t)=>{
                        this.watchers[e].push(t)
                    }
                    ,
                    this.handleCookieChange = ({changed: e, deleted: t})=>{
                        [...e, ...t].forEach((({domain: e, name: t, value: o})=>{
                            "upstox.com" === e && this.watchers[t] && this.watchers[t].forEach((e=>{
                                e(o ? "change" : "delete", t, o || null)
                            }
                            ))
                        }
                        ))
                    }
                    ,
                    this.setItem = (e,t,o)=>{
                        d().set(e, t, o)
                    }
                    ,
                    this.getItem = e=>d().get(e),
                    this.removeItem = (e,t=p)=>{
                        d().remove(e, t)
                    }
                    ,
                    window.cookieStore && (window.cookieStore.onchange = this.handleCookieChange)
                }
            }
              , h = Object.keys
              , g = {
                bod_version: 9
            }
              , f = {
                sidebarTab: 0,
                notificationOverlayActive: !1
            }
              , v = {
                logoutModal: !1
            };
            var E = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class y {
                constructor() {
                    this.initialized = !1,
                    this.config = {
                        ...g
                    },
                    this.theme = "light",
                    this.modalsConfig = v,
                    this.layout = c.getItem("UI_LAYOUT", !0) || f,
                    this.setTheme = e=>{
                        this.theme = e
                    }
                    ,
                    this.setInitialization = e=>{
                        this.initialized = e
                    }
                    ,
                    this.toggleModal = e=>{
                        h(this.modalsConfig).forEach((t=>{
                            t !== e && (this.modalsConfig[t] = !1)
                        }
                        )),
                        this.modalsConfig[e] = !this.modalsConfig[e]
                    }
                    ,
                    this.setConfig = e=>{
                        this.config = {
                            ...this.config,
                            ...e
                        }
                    }
                    ,
                    this.changeLayout = (e,t,o=!0)=>{
                        this.layout[e] = t,
                        o && c.setItem("UI_LAYOUT", this.layout)
                    }
                }
            }
            E([s.observable], y.prototype, "initialized", void 0),
            E([s.observable], y.prototype, "config", void 0),
            E([s.observable], y.prototype, "theme", void 0),
            E([s.observable], y.prototype, "modalsConfig", void 0),
            E([s.observable], y.prototype, "layout", void 0),
            E([s.action], y.prototype, "setTheme", void 0),
            E([s.action], y.prototype, "setInitialization", void 0),
            E([s.action], y.prototype, "toggleModal", void 0),
            E([s.action], y.prototype, "setConfig", void 0),
            E([s.action], y.prototype, "changeLayout", void 0);
            const b = new y;
            var T = o(34155);
            const P = "PROD"
              , w = "TRUE" === T.env.LOCAL
              , I = {
                UAT: {
                    redirect_uri: "https://uat-pro.upstox.com",
                    client_id: "PW3-Kd6pvTPIciPbPxdF5S3FAx88",
                    platform_id: "PW3"
                },
                PROD: {
                    redirect_uri: "https://pro.upstox.com",
                    client_id: "PW3-6Agd37PB52Q6B6DDpYWLuT7b",
                    platform_id: "PW3"
                },
                QA: {
                    redirect_uri: "https://qa-pro.upstox.com",
                    client_id: "PWQ-nMzE5W1elt03PHVJk2BxjzEj",
                    platform_id: "PW3"
                }
            }
              , x = {
                UAT: "wss://service-uat.upstox.com/login-ws/v1/login",
                QA: "wss://service.upstox.com/login-ws/v1/login",
                PROD: "wss://service.upstox.com/login-ws/v1/login"
            }
              , O = new class {
                constructor() {
                    this.isProduction = !0,
                    this.init = ()=>{
                        b.setInitialization(!0)
                    }
                }
            }
            ;
            var S = o(16550);
            const A = e=>{
                const t = r.useContext(n.yX);
                if (!t)
                    throw new Error("Store not found");
                return t[e]
            }
            ;
            var R = o(22698);
            const C = o.p + "assets/trading-view.svg"
              , k = o.p + "assets/pipe.svg"
              , _ = o.p + "assets/upstox-logo.svg";
            var N = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class D {
                constructor() {
                    this.notifications = [],
                    this.pushNotificationWithOverlay = e=>{
                        const t = {
                            ...e,
                            timeStamp: this.notifications.length
                        };
                        this.notifications = [...this.notifications, t]
                    }
                    ,
                    this.deleteNotificationWithOverlay = e=>{
                        const t = this.notifications.filter((t=>t.key !== e));
                        this.notifications = t
                    }
                }
            }
            N([s.observable], D.prototype, "notifications", void 0),
            N([s.action], D.prototype, "pushNotificationWithOverlay", void 0),
            N([s.action], D.prototype, "deleteNotificationWithOverlay", void 0);
            const L = new D;
            var V, U, q = o(94537), F = o(29697), M = o(59731), B = o(72986), W = o(17563), j = o(70401), Q = o.n(j), G = o(8891), z = o.n(G);
            !function(e) {
                e.LOGGED_IN = "Logged In",
                e.LOGIN_FAILED = "Login Failed",
                e.CHANGED_PIN = "Changed Pin",
                e.CHANGE_PIN_FAILED = "Change Pin Failed",
                e.TRY_TOTP = "Try TOTP clicked",
                e.ACCOUNT_DEACTIVATED = "Account Deactivated",
                e.ACCOUNT_REACTIVATED = "Account Reactivated",
                e.LOGIN_TO_1FA_TIME = "Login to 1FA Time Taken",
                e.OTP_TO_2FA_TIME = "1FA to 2FA Time Taken",
                e.ERROR_OCCURRED = "Login UI Error Occurred"
            }(V || (V = {})),
            function(e) {
                e.WEB = "WEB",
                e.TV = "TV"
            }(U || (U = {}));
            const $ = new class {
                constructor() {
                    this.token = "62597aa51842e6e2c56b97d96e4c5f8a",
                    this.serviceEnabled = !w,
                    this.config = {
                        api_host: "https://service.upstox.com/tracking-proxy/open/mp/events"
                    }
                }
                init() {
                    this.serviceEnabled && z().init(this.token, this.config)
                }
                setUser(e, t) {
                    this.serviceEnabled && (z().people.set({
                        "Profile ID": e
                    }),
                    z().people.set({
                        "Phone number": t
                    }),
                    z().identify(e))
                }
                sendEvent(e, t) {
                    this.serviceEnabled && z().track(e, t)
                }
            }
              , H = "/unlock-account"
              , K = {
                NEW_PRO_APP: {
                    PROD: "https://app.upstox.com",
                    QA: "https://qa-pro-4.upstox.com",
                    UAT: "https://uat-pro-4.upstox.com"
                },
                OLD_PRO_APP: {
                    PROD: "https://pro.upstox.com",
                    QA: "https://qa-pro.upstox.com",
                    UAT: "https://uat-pro.upstox.com"
                },
                UPSTOX_APP: {
                    PROD: "https://upstox.com/new-demat-account/profile",
                    QA: "https://upstox.com/new-demat-account/profile",
                    UAT: "https://uat.upstox.com/new-demat-account/profile"
                },
                WEBINAR_APP: {
                    PROD: "https://upstox.com/webinar",
                    QA: "https://upstox.com/webinar",
                    UAT: "https://uat.upstox.com/webinar"
                }
            };
            class Y extends B.RouterStore {
            }
            const X = new Y
              , J = (0,
            B.syncHistoryWithStore)((0,
            M.lX)(), X)
              , Z = new class {
                constructor() {
                    this.goToRoute = (e,t)=>{
                        let o = e;
                        (null == t ? void 0 : t.params) && (o = Object.entries(t.params).reduce(((e,[t,o])=>e.replace(`:${t}`, o)), o)),
                        (null == t ? void 0 : t.query) && (o = `${o}?${this.getQueryString(t.query)}`),
                        X.push(o)
                    }
                    ,
                    this.goBack = (e=!1)=>{
                        e ? X.history.goBack() : this.goBack()
                    }
                    ,
                    this.getQuery = (e=X.location.search)=>W.parse(e),
                    this.getQueryString = e=>(0,
                    W.stringify)(e) || "",
                    this.navigateOutside = e=>{
                        window.location.replace(e)
                    }
                    ,
                    this.openInNewTab = e=>window.open(e, "_blank"),
                    this.getExternalLinkByKey = e=>K[e][P],
                    this.isError = e=>"[object Error]" === Object.prototype.toString.call(e) || e instanceof Error,
                    this.createErrorObj = (e,t)=>{
                        const o = {
                            message: `${e.message || ""}`,
                            frames: []
                        };
                        return (null == t ? void 0 : t.length) && t.forEach((e=>{
                            const {columnNumber: t, lineNumber: r, fileName: i, functionName: n, source: s} = e;
                            let a = "<unknown>";
                            if (i) {
                                const e = i.indexOf("?");
                                e < 0 ? a = i : e > 0 && (a = i.substring(0, e))
                            }
                            o.frames.push({
                                src: s || "<unknown>",
                                line: r || 0,
                                col: t || 0,
                                fn: n || "<unknown>",
                                file: `${a}:${r || 0}:${t || 0}`
                            })
                        }
                        )),
                        o
                    }
                    ,
                    this.errorHandler = (e,{componentStack: t})=>{
                        w || (this.isError(e) ? Q().fromError(e, {
                            offline: !0
                        }).then((o=>{
                            const r = this.createErrorObj(e, o)
                              , {message: i="Unknown Error Occured", frames: n=[]} = r
                              , s = JSON.stringify(n);
                            $.sendEvent(V.ERROR_OCCURRED, {
                                Error: i,
                                "Component Stack Trace": s,
                                "Component Stack": t
                            })
                        }
                        )) : $.sendEvent(V.ERROR_OCCURRED, {
                            Error: "Unknown Error Occured",
                            "Component Stack": t
                        }))
                    }
                }
            }
              , ee = ({children: e})=>r.createElement(S.F0, {
                history: J
            }, e)
              , te = "https://help.upstox.com/support/home";
            class oe {
                constructor(e, t=3e3) {
                    this.callback = e,
                    this.delay = t,
                    this.timer = null,
                    this.start = ()=>{
                        if (this.timer)
                            throw Error("Timer is already started");
                        this.timerStartedTimeStamp = Date.now(),
                        this.timer = window.setTimeout(this.callback, this.delay)
                    }
                    ,
                    this.pause = ()=>{
                        if (this.timer) {
                            if (!this.timerStartedTimeStamp)
                                throw Error("Start timer before pause");
                            this.internalDelay = this.delay - (Date.now() - this.timerStartedTimeStamp),
                            clearTimeout(this.timer)
                        }
                    }
                    ,
                    this.stop = ()=>{
                        this.timer && (clearTimeout(this.timer),
                        this.timerStartedTimeStamp = void 0)
                    }
                    ,
                    this.resume = ()=>{
                        this.timer && (this.timerStartedTimeStamp = Date.now(),
                        this.timer = window.setTimeout(this.callback, this.internalDelay))
                    }
                }
            }
            const re = (0,
            n.Pi)((({id: e, title: t, icon: o, code: i, timeout: n})=>{
                var s, a, c;
                const {deleteNotificationWithOverlay: l} = A("NotificationStore")
                  , {current: u} = (0,
                r.useRef)(new oe((()=>{
                    u.stop(),
                    l(e)
                }
                ),n));
                (0,
                r.useEffect)((()=>{
                    u.start()
                }
                ), [n]);
                const d = {
                    1017074: {
                        title: "Multiple accounts are linked to this mobile number. Tap here, to know how to link a unique mobile number with each of your accounts",
                        onClick: ()=>Z.openInNewTab("https://help.upstox.com/support/solutions/articles/251906")
                    }
                };
                return r.createElement(R.Toast, {
                    onMouseOver: ()=>{
                        u.pause()
                    }
                    ,
                    onMouseLeave: ()=>{
                        u.resume()
                    }
                    ,
                    key: e,
                    before: o,
                    width: "full",
                    onClick: null === (s = d[i]) || void 0 === s ? void 0 : s.onClick
                }, r.createElement(R.Text, {
                    variant: "meta",
                    color: "text.3"
                }, null !== (c = null === (a = d[i]) || void 0 === a ? void 0 : a.title) && void 0 !== c ? c : t))
            }
            ))
              , ie = ()=>({
                position: "fixed",
                width: "100%",
                maxWidth: "328px",
                bottom: "30px",
                left: "50%",
                transform: "translate(-50%)"
            });
            var ne = o(66994)
              , se = o.n(ne)
              , ae = o(98733);
            se()(ae.Z, {
                insert: "head",
                singleton: !1
            }),
            ae.Z.locals;
            const ce = (0,
            n.Pi)((()=>{
                const {notifications: e} = A("NotificationStore")
                  , {changeLayout: t} = A("AppStore")
                  , o = e.length
                  , i = e=>{
                    switch (e) {
                    case "error":
                    default:
                        return r.createElement(R.ErrorCircleIcon, {
                            size: "large"
                        });
                    case "info":
                        return r.createElement(R.InfoIcon, {
                            size: "large"
                        });
                    case "success":
                        return r.createElement(R.CheckboxCheckedIcon, {
                            size: "large"
                        })
                    }
                }
                ;
                (0,
                r.useEffect)((()=>{
                    t("notificationOverlayActive", o > 0, !1)
                }
                ), [o, t]);
                const n = e.map((({key: e, title: t, type: o, text: r, date: n, icon: s, code: a, timeout: c},l)=>({
                    key: e,
                    timeStamp: l,
                    title: t,
                    type: o,
                    text: r,
                    date: n,
                    icon: s || i(o),
                    code: `${a}`,
                    timeout: c || 3e3
                })));
                return r.createElement(R.View, {
                    css: ie,
                    flexDirection: "column",
                    gap: "medium"
                }, r.createElement(q.Z, null, n.map((({key: e, ...t})=>r.createElement(F.Z, {
                    key: e,
                    timeout: 300,
                    classNames: "item"
                }, r.createElement(R.View, {
                    margin: [8, 0, 0]
                }, r.createElement(re, {
                    id: e,
                    ...t
                })))))))
            }
            ));
            var le = o(4511)
              , ue = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class de {
                constructor() {
                    this.step = m.getItem("lead_phone_number") ? 1 : 0,
                    this.goStepForward = (e=2)=>{
                        this.step !== e && (this.step += 1)
                    }
                    ,
                    this.goStepBack = ()=>{
                        0 !== this.step && (this.step -= 1)
                    }
                    ,
                    this.setStep = e=>{
                        this.step = e
                    }
                }
            }
            ue([s.observable], de.prototype, "step", void 0),
            ue([s.action], de.prototype, "goStepForward", void 0),
            ue([s.action], de.prototype, "goStepBack", void 0),
            ue([s.action], de.prototype, "setStep", void 0);
            const pe = de;
            var me = o(42238)
              , he = o.n(me);
            const ge = new class {
                constructor() {
                    this.isMobile = window.screen.width <= 768,
                    this.parser = new (he()),
                    this.device = this.parser.getDevice(),
                    this.browser = this.parser.getBrowser(),
                    this.os = this.parser.getOS(),
                    this.getDeviceDetails = ()=>{
                        var e, t, o;
                        return {
                            manufacturer: null !== (t = null === (e = this.device) || void 0 === e ? void 0 : e.vendor) && void 0 !== t ? t : "unknown",
                            osName: `${this.os.name}/${this.os.version}`,
                            osVersion: `${this.browser.name}/${this.browser.version}`,
                            browserName: null !== (o = this.browser.name) && void 0 !== o ? o : "unknown"
                        }
                    }
                }
            }
              , fe = "Let’s get started"
              , ve = {
                loading: !1,
                error: !1,
                success: !1,
                qrContent: "",
                reloadQr: !1
            }
              , Ee = {
                validityInSeconds: 30,
                qrCodeAutoRefreshPendingCount: 5
            };
            var ye = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class be extends pe {
                constructor() {
                    var e;
                    super(...arguments),
                    this.isProWeb4App = !1,
                    this.isTradingViewApp = !1,
                    this.isIPOApp = !1,
                    this.mobileNumber = null !== (e = m.getItem("lead_phone_number")) && void 0 !== e ? e : "",
                    this.hasSecretPin = Boolean(l.getItem("HAS_SECRET_PIN")) || !1,
                    this.otpRequestInterval = 120,
                    this.userProfile = l.getItem("USER_PROFILE", !0),
                    this.userType = m.getItem("user_type"),
                    this.userId = "",
                    this.profileId = "",
                    this.clientId = "",
                    this.redirectUrl = "",
                    this.platformId = "",
                    this.application_type = "",
                    this.isRedirecting = !1,
                    this.workflow = "",
                    this.workflowVersion = "",
                    this.landingPage = "",
                    this.referralCode = "",
                    this.utmParams = null,
                    this.isUnlockAccount = !1,
                    this.previousStep = 0,
                    this.loginTo1FATime = 0,
                    this.otpTo2FATime = 0,
                    this.isQRLoginEnabled = !1,
                    this.isTotpLoginEnabled = !1,
                    this.qrConfig = null,
                    this.redirectPath = "",
                    this.devRedirectUri = null,
                    this.redirectQuery = "",
                    this.watchUserProfile = (0,
                    s.autorun)((()=>l.sync("USER_PROFILE", this.userProfile))),
                    this.setIsUnlockAccount = e=>{
                        this.isUnlockAccount = e
                    }
                    ,
                    this.setMobileNumber = e=>{
                        this.mobileNumber = e
                    }
                    ,
                    this.setOtpRequestInterval = e=>{
                        this.otpRequestInterval = e
                    }
                    ,
                    this.setHasSecretPin = e=>{
                        e && l.setItem("AUTH_IDENTITY_SET", !0),
                        l.setItem("HAS_SECRET_PIN", e),
                        this.hasSecretPin = e
                    }
                    ,
                    this.setUserType = e=>{
                        this.userType = e
                    }
                    ,
                    this.setPreviousStep = e=>{
                        this.previousStep = e
                    }
                    ,
                    this.setIsRedirecting = e=>{
                        this.isRedirecting = e
                    }
                    ,
                    this.setUserProfile = e=>{
                        this.userProfile = e,
                        l.setItem("USER_PROFILE", e)
                    }
                    ,
                    this.setUserId = e=>{
                        this.userId = e
                    }
                    ,
                    this.setProfileId = e=>{
                        this.profileId = String(e),
                        l.setItem("PROFILE_ID", e)
                    }
                    ,
                    this.setRedirectUrl = e=>{
                        this.redirectUrl = e
                    }
                    ,
                    this.setClientId = e=>{
                        this.clientId = e
                    }
                    ,
                    this.setIsProWeb4App = e=>{
                        this.isProWeb4App = e
                    }
                    ,
                    this.setIsTradingViewApp = e=>{
                        this.isTradingViewApp = e
                    }
                    ,
                    this.setIsIPOApp = e=>{
                        this.isIPOApp = e
                    }
                    ,
                    this.setLoginTo1FATime = e=>{
                        this.loginTo1FATime = e
                    }
                    ,
                    this.setOtpTo2FATime = e=>{
                        this.otpTo2FATime = e
                    }
                    ,
                    this.setQrLoginEnabled = e=>{
                        this.isQRLoginEnabled = e && !ge.isMobile
                    }
                    ,
                    this.setTotpLoginEnabled = e=>{
                        this.isTotpLoginEnabled = e
                    }
                    ,
                    this.setQrConfig = e=>{
                        this.qrConfig = e
                    }
                    ,
                    this.setLoginCredentials = ({client_id: e=I[P].client_id, platform_id: t=I[P].platform_id, redirect_uri: o=I[P].redirect_uri, workflow: r, workflow_version: i, dev_redirect_uri: n, redirect_path: s, redirect_query: a, application_type: c, utm_campaign: l, utm_content: u, utm_term: d, utm_medium: p, utm_referer: m, utm_source: h, utm_unique_id: g, landing_page: f, referral_code: v, phone_number: E})=>{
                        this.setRedirectUrl(o),
                        this.setClientId(e),
                        this.platformId = t;
                        const y = e.includes("PW4")
                          , b = "PW3" === t
                          , T = "UTV" === t;
                        this.setIsProWeb4App(y),
                        this.setIsTradingViewApp(T),
                        n && (this.devRedirectUri = n),
                        s && !s.includes("@") && s.startsWith("/") && (this.redirectPath = s),
                        r && (this.workflow = r),
                        i && (this.workflowVersion = i),
                        f && (this.landingPage = f),
                        c && (this.application_type = c),
                        v && (this.referralCode = v),
                        E && (this.mobileNumber = E),
                        (l || h || u || d || p || m || g) && (this.utmParams = {
                            utm_campaign: l || "",
                            utm_content: u || "",
                            utm_term: d || "",
                            utm_medium: p || "",
                            utm_referer: m || "",
                            utm_source: h || "",
                            utm_unique_id: g || ""
                        }),
                        a && (this.redirectQuery = b ? Z.getQueryString(JSON.parse(atob(a))) : atob(a))
                    }
                    ,
                    this.reset = ()=>{
                        this.setUserId(""),
                        this.setProfileId(""),
                        this.setHasSecretPin(!1),
                        this.setStep(0),
                        this.setUserProfile(null),
                        this.setPreviousStep(0),
                        this.setMobileNumber(""),
                        this.setLoginTo1FATime(0),
                        this.setOtpTo2FATime(0),
                        l.removeItem("HAS_SECRET_PIN"),
                        l.removeItem("AUTH_IDENTITY_SET"),
                        l.removeItem("USER_ID"),
                        l.removeItem("PROFILE_ID"),
                        l.removeItem("USER_PROFILE"),
                        l.removeItem("MOBILE_NUMBER"),
                        m.removeItem("customer_status"),
                        m.removeItem("profile_id"),
                        m.removeItem("user_type")
                    }
                }
                get getPinRequestHeaders() {
                    return {
                        "X-Profile-Id": this.profileId,
                        "X-User-Id": this.userId
                    }
                }
                get pinRequestsQuery() {
                    return {
                        client_id: this.clientId,
                        redirect_uri: this.isIPOApp ? `${this.redirectUrl}?${this.redirectQuery}` : this.redirectUrl
                    }
                }
                get isReturnedUser() {
                    return "CUSTOMER" === this.userType && null !== this.getUserProfile
                }
                get profileDetails() {
                    if (this.userProfile) {
                        const {firstName: e, lastName: t, avatarUrl: o} = this.userProfile;
                        return {
                            fullName: `${e} ${t}`,
                            avatar: o
                        }
                    }
                    return {
                        fullName: "",
                        avatar: null
                    }
                }
                get getUserType() {
                    return this.userType || "CUSTOMER"
                }
                get isLead() {
                    return "LEAD" === this.getUserType
                }
                get getUserProfile() {
                    return this.userProfile
                }
                get userFirstName() {
                    var e;
                    if (this.userProfile)
                        return null === (e = this.userProfile.firstName) || void 0 === e ? void 0 : e.toLowerCase()
                }
                get referralBody() {
                    var e, t, o;
                    if (this.landingPage || this.referralCode || this.utmParams)
                        return {
                            ...this.isIPOApp && {
                                applicationType: this.application_type
                            },
                            onboardingDetails: {
                                landingPage: null !== (e = this.landingPage) && void 0 !== e ? e : "",
                                referralCode: null !== (t = this.referralCode) && void 0 !== t ? t : "",
                                utmParams: null !== (o = this.utmParams) && void 0 !== o ? o : {}
                            }
                        }
                }
            }
            ye([s.observable], be.prototype, "isProWeb4App", void 0),
            ye([s.observable], be.prototype, "isTradingViewApp", void 0),
            ye([s.observable], be.prototype, "isIPOApp", void 0),
            ye([s.observable], be.prototype, "mobileNumber", void 0),
            ye([s.observable], be.prototype, "hasSecretPin", void 0),
            ye([s.observable], be.prototype, "otpRequestInterval", void 0),
            ye([s.observable], be.prototype, "userProfile", void 0),
            ye([s.observable], be.prototype, "userType", void 0),
            ye([s.observable], be.prototype, "userId", void 0),
            ye([s.observable], be.prototype, "profileId", void 0),
            ye([s.observable], be.prototype, "clientId", void 0),
            ye([s.observable], be.prototype, "redirectUrl", void 0),
            ye([s.observable], be.prototype, "platformId", void 0),
            ye([s.observable], be.prototype, "application_type", void 0),
            ye([s.observable], be.prototype, "isRedirecting", void 0),
            ye([s.observable], be.prototype, "workflow", void 0),
            ye([s.observable], be.prototype, "workflowVersion", void 0),
            ye([s.observable], be.prototype, "landingPage", void 0),
            ye([s.observable], be.prototype, "referralCode", void 0),
            ye([s.observable], be.prototype, "utmParams", void 0),
            ye([s.observable], be.prototype, "isUnlockAccount", void 0),
            ye([s.observable], be.prototype, "previousStep", void 0),
            ye([s.observable], be.prototype, "loginTo1FATime", void 0),
            ye([s.observable], be.prototype, "otpTo2FATime", void 0),
            ye([s.observable], be.prototype, "isQRLoginEnabled", void 0),
            ye([s.observable], be.prototype, "isTotpLoginEnabled", void 0),
            ye([s.observable], be.prototype, "qrConfig", void 0),
            ye([s.action], be.prototype, "setIsUnlockAccount", void 0),
            ye([s.action], be.prototype, "setMobileNumber", void 0),
            ye([s.action], be.prototype, "setOtpRequestInterval", void 0),
            ye([s.action], be.prototype, "setHasSecretPin", void 0),
            ye([s.action], be.prototype, "setUserType", void 0),
            ye([s.action], be.prototype, "setPreviousStep", void 0),
            ye([s.action], be.prototype, "setIsRedirecting", void 0),
            ye([s.action], be.prototype, "setUserProfile", void 0),
            ye([s.action], be.prototype, "setUserId", void 0),
            ye([s.action], be.prototype, "setProfileId", void 0),
            ye([s.action], be.prototype, "setRedirectUrl", void 0),
            ye([s.action], be.prototype, "setClientId", void 0),
            ye([s.action], be.prototype, "setIsProWeb4App", void 0),
            ye([s.action], be.prototype, "setIsTradingViewApp", void 0),
            ye([s.action], be.prototype, "setIsIPOApp", void 0),
            ye([s.action], be.prototype, "setLoginTo1FATime", void 0),
            ye([s.action], be.prototype, "setOtpTo2FATime", void 0),
            ye([s.action], be.prototype, "setQrLoginEnabled", void 0),
            ye([s.action], be.prototype, "setTotpLoginEnabled", void 0),
            ye([s.action], be.prototype, "setQrConfig", void 0),
            ye([s.action], be.prototype, "setLoginCredentials", void 0),
            ye([s.action], be.prototype, "reset", void 0),
            ye([s.computed], be.prototype, "getPinRequestHeaders", null),
            ye([s.computed], be.prototype, "pinRequestsQuery", null),
            ye([s.computed], be.prototype, "isReturnedUser", null),
            ye([s.computed], be.prototype, "profileDetails", null),
            ye([s.computed], be.prototype, "getUserType", null),
            ye([s.computed], be.prototype, "isLead", null),
            ye([s.computed], be.prototype, "getUserProfile", null),
            ye([s.computed], be.prototype, "userFirstName", null),
            ye([s.computed], be.prototype, "referralBody", null);
            const Te = new be;
            var Pe = o(27484)
              , we = o.n(Pe)
              , Ie = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class xe {
                constructor() {
                    this.loadings = {},
                    this.setLoading = (e,t)=>{
                        this.loadings[e] = t
                    }
                }
            }
            Ie([s.observable], xe.prototype, "loadings", void 0),
            Ie([s.action], xe.prototype, "setLoading", void 0);
            const Oe = new xe;
            var Se = o(1646)
              , Ae = o.n(Se)
              , Re = o(64296);
            const Ce = "DD/MM/YYYY";
            we().extend(Ae());
            const ke = new class {
                constructor() {
                    this.nanoid = (0,
                    Re.customAlphabet)("1234567890abcdef", 10),
                    this.generateUniqueId = ()=>this.nanoid(),
                    this.formatSeconds = (e,t)=>we().duration(+e, "seconds").format(t),
                    this.formatOtp = e=>e.replace(/\D+/, ""),
                    this.generateErrorMessage = (e,t)=>`${e} [${t}]`,
                    this.mobileNumberValidationMessage = (e,t)=>{
                        if (e) {
                            if (10 === t.length)
                                return "Make sure your mobile number was entered correctly.";
                            if (t.length > 0)
                                return "Enter a 10-digit mobile number."
                        }
                    }
                }
                formatDate(e, t="D MMM YYYY MM:HH") {
                    return we()(e).format(Ce) === we()().format(Ce) && "D MMM YYYY" === t ? "Today" : we()(e).format(t)
                }
            }
            ;
            var _e = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class Ne {
                constructor() {
                    this.server = {},
                    this.setServerError = (e,t)=>{
                        this.server[e] = t
                    }
                    ,
                    this.clearErrors = ()=>{
                        this.server = {}
                    }
                    ,
                    this.clearErrorByKey = e=>{
                        delete this.server[e]
                    }
                }
            }
            _e([s.observable], Ne.prototype, "server", void 0),
            _e([s.action], Ne.prototype, "setServerError", void 0),
            _e([s.action], Ne.prototype, "clearErrors", void 0),
            _e([s.action], Ne.prototype, "clearErrorByKey", void 0);
            const De = new Ne
              , Le = {
                AWS_UPSTOX: {
                    paths: ["/platform/web"],
                    proxy: {
                        PROD: "https://upstoxpro.s3.ap-south-1.amazonaws.com",
                        UAT: "https://upstoxpro.s3.ap-south-1.amazonaws.com",
                        QA: "https://upstoxpro.s3.ap-south-1.amazonaws.com"
                    }
                },
                LOGOUT: {
                    paths: ["/logout"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/open/v3/auth",
                        UAT: "https://service-uat.upstox.com/login/open/v3/auth",
                        QA: "https://service.upstox.com/login/open/v3/auth"
                    }
                },
                "1FA_OTP": {
                    paths: ["/v5/auth/1fa/otp/generate", "/v4/auth/1fa/otp-totp/verify", "/v3/auth/ipo/otp/verify"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/open",
                        UAT: "https://service-uat.upstox.com/login/open",
                        QA: "https://service.upstox.com/login/open"
                    }
                },
                "2FA": {
                    paths: ["/2fa", "/2fa/secret-pin/set", "/2fa/secret-pin/forgot/set-new-pin", "/2fa/yob"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/open/v3/auth",
                        UAT: "https://service-uat.upstox.com/login/open/v3/auth",
                        QA: "https://service.upstox.com/login/open/v3/auth"
                    }
                },
                VERIFY_IDENTITY_TOKEN: {
                    paths: ["/"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/open/v3/auth/gateway-worker/v1/verify-auth-identity-token",
                        UAT: "https://service-uat.upstox.com/login/open/v3/auth/gateway-worker/v1/verify-auth-identity-token",
                        QA: "https://service.upstox.com/login/open/v3/auth/gateway-worker/v1/verify-auth-identity-token"
                    }
                },
                FORGOT_PIN_OTP: {
                    paths: ["/2fa/secret-pin/forgot", "/2fa/secret-pin/forgot/otp/verify", "/ipo/otp/verify"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/open/v3/auth",
                        UAT: "https://service-uat.upstox.com/login/open/v3/auth",
                        QA: "https://service.upstox.com/login/open/v3/auth"
                    }
                },
                LEAD_LOGIN: {
                    paths: ["/leads/2fa"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/open/v1/auth",
                        UAT: "https://service-uat.upstox.com/login/open/v1/auth",
                        QA: "https://service.upstox.com/login/open/v1/auth"
                    }
                },
                AUTOLOGIN: {
                    paths: ["/submit"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/open/v2/auth/auto-login",
                        UAT: "https://service-uat.upstox.com/login/open/v2/auth/auto-login",
                        QA: "https://service.upstox.com/login/open/v2/auth/auto-login"
                    }
                },
                AUTOLOGINQR: {
                    paths: ["/auto-login/submit"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/open/v3/auth",
                        UAT: "https://service-uat.upstox.com/login/open/v3/auth",
                        QA: "https://service.upstox.com/login/open/v3/auth"
                    }
                },
                DEACTIVATION: {
                    paths: ["/validate-deactivate-account", "/generate-otp", "/verify-otp"],
                    proxy: {
                        PROD: "https://service.upstox.com/account-management/v0",
                        UAT: "https://service-uat.upstox.com/account-management/v0",
                        QA: "https://service.upstox.com/account-management/v0"
                    }
                },
                REACTIVATION: {
                    paths: ["/reactivate-account", "/reactivation-details"],
                    proxy: {
                        PROD: "https://service.upstox.com/account-management/v0",
                        UAT: "https://service-uat.upstox.com/account-management/v0",
                        QA: "https://service.upstox.com/account-management/v0"
                    }
                },
                AUTH: {
                    paths: ["/authorize", "/client-app"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/v2/oauth",
                        UAT: "https://service-uat.upstox.com/login/v2/oauth",
                        QA: "https://service.upstox.com/login/v2/oauth"
                    }
                },
                REFRESH_ACCESS_TOKEN: {
                    paths: ["/refresh-access-token"],
                    proxy: {
                        PROD: "https://service.upstox.com/login/open/v3/auth",
                        UAT: "https://service-uat.upstox.com/login/open/v3/auth",
                        QA: "https://service.upstox.com/login/open/v3/auth"
                    }
                }
            }
              , Ve = {
                success: !1,
                data: null,
                error: {
                    code: 500,
                    message: "Something went wrong"
                }
            }
              , Ue = new class {
                constructor() {
                    this.deviceDetails = ()=>{
                        const {osName: e, osVersion: t, browserName: o, manufacturer: r} = ge.getDeviceDetails();
                        return `platform=WEB|osName=${e}|osVersion=${t}|appVersion=4.0.0|modelName=${o}|manufacturer=${r}`
                    }
                    ,
                    this.defaultHeaders = {
                        "Content-Type": "application/json",
                        "X-Device-Details": this.deviceDetails()
                    },
                    this.activeRequests = {},
                    this.request = async(e,t,o,r={},i=!1)=>{
                        var n;
                        const {method: s="GET", headers: a={}, query: c={}, pathParameter: l, overrideCredentials: u, body: d, overrideHeaders: p, addRequestIdHeader: m=!0} = r
                          , h = this.getQueryString({
                            ...c
                        })
                          , g = this.configurePath(t, l)
                          , f = `${Le[e].proxy[P]}${g}${h}`
                          , {signal: v} = this.registerRequest(o)
                          , E = {
                            method: s,
                            signal: v,
                            headers: this.getRequestHeaders(a, p, m),
                            mode: "cors",
                            credentials: u || "include"
                        };
                        d && (E.body = JSON.stringify(d));
                        try {
                            const e = await fetch(f, E)
                              , t = await e.json();
                            if (this.unregisterRequest(o, i),
                            !1 === t.success || t.error)
                                switch (null === (n = t.error) || void 0 === n ? void 0 : n.code) {
                                case 1017105:
                                case 1017095:
                                case 1017079:
                                case 1017084:
                                    Te.reset(),
                                    X.push("/"),
                                    De.setServerError(o, t.error);
                                    break;
                                default:
                                    De.setServerError(o, t.error)
                                }
                            return t
                        } catch (e) {
                            return this.unregisterRequest(o),
                            De.setServerError(o, {
                                message: "Request aborted",
                                code: 500
                            }),
                            {
                                ...Ve,
                                error: {
                                    code: 500,
                                    message: "Request aborted"
                                }
                            }
                        }
                    }
                    ,
                    this.requestStatic = async(e,t,o,r={})=>this.request(e, t, o, {
                        ...r,
                        headers: {
                            "Content-Type": "text/plain"
                        },
                        overrideHeaders: !0
                    }),
                    this.getRequestHeaders = (e,t,o)=>t ? e : {
                        ...this.defaultHeaders,
                        ...e,
                        ...o && {
                            "X-Request-ID": `WPRO-${ke.generateUniqueId()}`
                        }
                    },
                    this.getQueryString = e=>{
                        const t = (0,
                        W.stringify)(e);
                        return t ? `?${t}` : ""
                    }
                    ,
                    this.registerRequest = e=>(this.activeRequests[e] && this.unregisterController(e),
                    this.activeRequests[e] = new AbortController,
                    Oe.setLoading(e, !0),
                    this.activeRequests[e]),
                    this.unregisterController = e=>{
                        const t = this.activeRequests[e];
                        t && t.abort()
                    }
                    ,
                    this.unregisterRequest = (e,t=!1)=>{
                        t || Oe.setLoading(e, !1),
                        this.activeRequests[e] = void 0
                    }
                    ,
                    this.configurePath = (e,t)=>t ? `${e}/${t}` : e
                }
            }
            ;
            var qe = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class Fe {
                constructor() {
                    this.verifyOtpToken = "",
                    this.otp = "",
                    this.infoMessage = "",
                    this.otpErrors = {},
                    this.setVerifyOtpToken = e=>{
                        this.verifyOtpToken = e
                    }
                    ,
                    this.setOtp = e=>{
                        this.otp = e
                    }
                    ,
                    this.setInfoMessage = e=>{
                        this.infoMessage = e
                    }
                    ,
                    this.clearOtpErrors = ()=>{
                        this.otpErrors = {}
                    }
                    ,
                    this.setOtpError = (e,t)=>{
                        this.otpErrors[e] = t
                    }
                }
                get isOtpValid() {
                    return !Object.values(this.otpErrors).filter(Boolean).length
                }
            }
            qe([s.observable], Fe.prototype, "verifyOtpToken", void 0),
            qe([s.observable], Fe.prototype, "otp", void 0),
            qe([s.observable], Fe.prototype, "infoMessage", void 0),
            qe([s.observable], Fe.prototype, "otpErrors", void 0),
            qe([s.action], Fe.prototype, "setVerifyOtpToken", void 0),
            qe([s.action], Fe.prototype, "setOtp", void 0),
            qe([s.action], Fe.prototype, "setInfoMessage", void 0),
            qe([s.action], Fe.prototype, "clearOtpErrors", void 0),
            qe([s.action], Fe.prototype, "setOtpError", void 0),
            qe([s.computed], Fe.prototype, "isOtpValid", null);
            const Me = new Fe
              , Be = {
                "1FA_OTP": {
                    generateOtpPath: "/v5/auth/1fa/otp/generate",
                    verifyOtpPath: "/v4/auth/1fa/otp-totp/verify",
                    verifyTokenFieldName: "validateOtpToken",
                    verifyOtpPathIPO: "/v3/auth/ipo/otp/verify"
                },
                FORGOT_PIN_OTP: {
                    generateOtpPath: "/2fa/secret-pin/forgot",
                    verifyOtpPath: "/2fa/secret-pin/forgot/otp/verify",
                    verifyTokenFieldName: "forgotSecretPinToken",
                    verifyOtpPathIPO: "/ipo/otp/verify"
                }
            }
              , We = "We sent a 6-digit OTP to your phone number"
              , je = 1017078
              , Qe = new class {
                constructor() {
                    this.initOtpService = e=>{
                        this.configKey = e
                    }
                    ,
                    this.clearOtpServiceData = ()=>{
                        this.configKey = void 0,
                        Me.setOtp(""),
                        Me.setInfoMessage(""),
                        Me.clearOtpErrors()
                    }
                    ,
                    this.validateOtp = ()=>{
                        Me.clearOtpErrors(),
                        6 !== ke.formatOtp(Me.otp).length && Me.setOtpError("otpLength", !0)
                    }
                    ,
                    this.verifyOtpRequest = async(e,t)=>{
                        if (!this.configKey)
                            return;
                        if (this.validateOtp(),
                        !Me.isOtpValid)
                            return;
                        const {verifyOtpPath: o, verifyTokenFieldName: r, verifyOtpPathIPO: i} = Be[this.configKey]
                          , n = ke.formatOtp(Me.otp)
                          , s = Te.isIPOApp
                          , a = s ? i : o
                          , c = await Ue.request(this.configKey, a, this.configKey, {
                            method: "POST",
                            ...s && {
                                query: Te.pinRequestsQuery
                            },
                            body: {
                                data: {
                                    otp: n,
                                    [r]: Me.verifyOtpToken,
                                    ...t
                                }
                            }
                        });
                        c.success ? (L.pushNotificationWithOverlay({
                            key: this.configKey,
                            title: null == c ? void 0 : c.data.message,
                            type: "success"
                        }),
                        e && (Me.setOtp(""),
                        e(c.data))) : L.pushNotificationWithOverlay({
                            key: this.configKey,
                            title: ke.generateErrorMessage(c.error.message, c.error.code),
                            type: "error"
                        })
                    }
                }
            }
              , Ge = {
                position: "relative"
            }
              , ze = (0,
            n.Pi)((({otpConfigKey: e, onOtpVerifiedCallback: t, additionalData: o, bottomIcon: i, tryTotpInfo: n})=>{
                const {otp: s, setOtp: a, isOtpValid: c} = A("OtpStore")
                  , {isTotpLoginEnabled: l, setOtpTo2FATime: u} = A("AuthStore")
                  , {server: {"1FA_OTP": d, FORGOT_PIN_OTP: p}, clearErrorByKey: m} = A("ErrorStore")
                  , {loadings: {[e]: h}} = A("LoadingStore");
                (0,
                r.useEffect)((()=>Qe.clearOtpServiceData), []),
                (0,
                r.useEffect)((()=>()=>{
                    m("1FA_OTP"),
                    m("FORGOT_PIN_OTP")
                }
                ), [m]),
                (0,
                r.useEffect)((()=>{
                    Qe.initOtpService(e)
                }
                ), [e]);
                const g = (null == d ? void 0 : d.code) === je || 1017125 === (null == d ? void 0 : d.code) || (null == p ? void 0 : p.code) === je
                  , f = s.length <= 6 && s.length > 0
                  , v = l && "1FA_OTP" === e ? "Enter OTP or TOTP" : "Enter OTP";
                return r.createElement(R.View, {
                    as: "form",
                    flexDirection: "column",
                    id: "otp-form",
                    onSubmit: e=>{
                        e.preventDefault(),
                        u(Date.now()),
                        Qe.verifyOtpRequest(t, o)
                    }
                    ,
                    flex: !0
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    padding: [0, 16, 16],
                    margin: [0, 0, 16]
                }, r.createElement(R.View, {
                    inline: !1,
                    flexDirection: i ? "column" : "row",
                    style: n ? Ge : {}
                }, r.createElement(R.MaskedInput, {
                    as: R.InputField,
                    mask: [/\d/, /\d/, /\d/, "-", /\d/, /\d/, /\d/],
                    guide: !1,
                    disabled: h || g,
                    type: "text",
                    label: v,
                    value: s,
                    onChange: e=>{
                        a(e.target.value)
                    }
                    ,
                    error: (!c || f) && "It should be a 6-digit OTP.",
                    variant: "secondary",
                    InputProps: {
                        autoFocus: !0,
                        id: "otpNum"
                    },
                    flex: !0
                }), i && i, n && n), g && r.createElement(R.View, {
                    margin: [20, 0, 0]
                }, r.createElement(R.Alert, {
                    variant: "warning",
                    cardVariant: "primary",
                    icon: r.createElement(R.ErrorCircleIcon, {
                        size: "large"
                    }),
                    title: r.createElement(R.Text, {
                        variant: "meta"
                    }, (null == d ? void 0 : d.message) || (null == p ? void 0 : p.message))
                }))), r.createElement(R.View, {
                    padding: [0, 0, 20]
                }, r.createElement(R.Button, {
                    width: "full",
                    variant: "primary",
                    type: "submit",
                    isLoading: h,
                    disabled: !s.length || g,
                    id: "continueBtn"
                }, "Continue")))
            }
            ))
              , $e = e=>{
                const [t,o] = (0,
                r.useState)(e);
                return (0,
                r.useEffect)((()=>{
                    const e = setInterval((()=>{
                        o((e=>e <= 0 ? 0 : e - 1))
                    }
                    ), 1e3);
                    return ()=>clearInterval(e)
                }
                ), []),
                [t, o]
            }
            ;
            var He, Ke;
            !function(e) {
                e[e.UserId = 0] = "UserId",
                e[e.OtpVerification = 1] = "OtpVerification",
                e[e.PasswordReset = 2] = "PasswordReset",
                e[e.SuccessfullReset = 3] = "SuccessfullReset"
            }(He || (He = {})),
            function(e) {
                e.LEAD = "MOBILE",
                e.CUSTOMER = "PAN_NUMBER"
            }(Ke || (Ke = {}));
            const Ye = new class {
                constructor() {
                    this.isLength = (e,t,o)=>!(t && e.length < t || o && e.length > o),
                    this.isIndiaPhoneNumber = e=>/^[6,7,8,9]\d{9}$/.test(e),
                    this.isPANCard = e=>/^[a-zA-Z]{5}\d{4}[a-zA-Z]{1}$/.test(e),
                    this.isEmail = e=>/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(e)
                }
                hasSpecialChar(e) {
                    return /[!@#$%*+-=]/g.test(e)
                }
                hasNumber(e) {
                    return /\d/.test(e)
                }
                hasAlpha(e) {
                    return /[a-z]+/.test(e)
                }
                hasUppercase(e) {
                    return /[A-Z]+/.test(e)
                }
                passwordStrength(e) {
                    const t = {
                        valid: !1,
                        percentage: 0,
                        steps: {
                            hasSpecialChar: !1,
                            hasNumber: !1,
                            hasAlpha: !1,
                            hasUppercase: !1,
                            validLength: !1
                        }
                    }
                      , o = 100 / Object.keys(t.steps).length
                      , r = e=>{
                        const {steps: r} = t;
                        r[e] = !0,
                        t.percentage += o,
                        r.hasNumber && r.hasSpecialChar && r.validLength && r.hasAlpha && r.hasUppercase && (t.valid = !0,
                        t.percentage = 100)
                    }
                    ;
                    return this.isLength(e, 8, 12) && r("validLength"),
                    this.hasSpecialChar(e) && r("hasSpecialChar"),
                    this.hasNumber(e) && r("hasNumber"),
                    this.hasAlpha(e) && r("hasAlpha"),
                    this.hasUppercase(e) && r("hasUppercase"),
                    t
                }
            }
              , Xe = ({cssProps: {isButtonDisabled: e}})=>({
                alignSelf: "end",
                cursor: e ? "not-allowed" : "pointer"
            })
              , Je = (0,
            n.Pi)((({resendOtpRequest: e})=>{
                const {otpRequestInterval: t, isQRLoginEnabled: o} = A("AuthStore")
                  , {setOtp: i} = A("OtpStore")
                  , {server: {"1FA_OTP": n, FORGOT_PIN_OTP: s}, clearErrorByKey: a} = A("ErrorStore")
                  , [c,l] = $e(t)
                  , [u,d] = $e(0)
                  , [p,m] = (0,
                r.useState)(!1)
                  , h = (0,
                r.useMemo)((()=>(null == n ? void 0 : n.code) === je || (null == s ? void 0 : s.code) === je), [n, s]);
                (0,
                r.useEffect)((()=>{
                    h && (l(0),
                    d(600),
                    m(!0))
                }
                ), [h, d, l, a]);
                const g = h && !p || u > 0
                  , f = ()=>{
                    g || (l(t),
                    i(""),
                    e(!0),
                    a("1FA_OTP"),
                    a("FORGOT_PIN_OTP"))
                }
                  , v = o ? r.createElement(R.View, {
                    as: "div",
                    onClick: f,
                    css: Xe,
                    cssProps: {
                        isButtonDisabled: g
                    }
                }, r.createElement(R.Text, {
                    variant: "bodyBold",
                    color: g ? "disabled.2" : "text.link"
                }, "Resend OTP")) : r.createElement(R.Button, {
                    variant: "invisible",
                    disabled: g,
                    onClick: f
                }, r.createElement(R.Text, {
                    variant: "bodyBold",
                    color: g ? "disabled.2" : "text.link"
                }, "Resend OTP"));
                return c ? r.createElement(R.Text, {
                    variant: "bodyBold",
                    color: "disabled.2"
                }, "Resend OTP (", ke.formatSeconds(c, "m:ss"), "s)") : v
            }
            ));
            var Ze = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class et extends pe {
                constructor() {
                    super(...arguments),
                    this.pan = "",
                    this.mobileNumber = "",
                    this.previousStep = 0,
                    this.setPAN = e=>{
                        this.pan = e
                    }
                    ,
                    this.setMobileNumber = e=>{
                        this.mobileNumber = e
                    }
                    ,
                    this.setPreviousStep = e=>{
                        this.previousStep = e
                    }
                    ,
                    this.clear = ()=>{
                        this.setPAN(""),
                        this.setMobileNumber("")
                    }
                }
            }
            Ze([s.observable], et.prototype, "pan", void 0),
            Ze([s.observable], et.prototype, "mobileNumber", void 0),
            Ze([s.observable], et.prototype, "previousStep", void 0),
            Ze([s.action], et.prototype, "setPAN", void 0),
            Ze([s.action], et.prototype, "setMobileNumber", void 0),
            Ze([s.action], et.prototype, "setPreviousStep", void 0),
            Ze([s.action], et.prototype, "clear", void 0);
            const tt = new et
              , ot = new class {
                constructor() {
                    this.stepReaction = (0,
                    s.reaction)((()=>tt.step), (e=>{
                        e === tt.previousStep && 0 !== e && this.generateOtpRequest(!1, !0)
                    }
                    )),
                    this.generateOtpRequest = async(e=!1,t=!1)=>{
                        const o = await Ue.request("FORGOT_PIN_OTP", "/2fa/secret-pin/forgot", "FORGOT_PIN_OTP", {
                            method: "POST",
                            body: {
                                data: this.generateRecoveryBody
                            }
                        });
                        if (o.success && (Me.setVerifyOtpToken(o.data.forgotSecretPinToken),
                        Me.setInfoMessage(o.data.message),
                        e ? L.pushNotificationWithOverlay({
                            key: "OTP_RESEND",
                            type: "info",
                            title: "OTP has been resent to your Phone!"
                        }) : (t || tt.goStepForward(1),
                        X.location.pathname === H && Z.goToRoute("/forgot-pin"))),
                        o.error)
                            switch (o.error.code) {
                            case 1017107:
                                this.pushErrorNotification("FORGOT_PIN_PAN_VALIDATION_FAILED", o.error.message, o.error.code);
                                break;
                            case 1017108:
                                this.pushErrorNotification("FORGOT_PIN_MOBILE_VALIDATION_FAILED", o.error.message, o.error.code);
                                break;
                            default:
                                this.pushErrorNotification("FORGOT_PIN_OTP", o.error.message, o.error.code)
                            }
                    }
                    ,
                    this.pushErrorNotification = (e,t,o)=>{
                        L.pushNotificationWithOverlay({
                            key: e,
                            title: ke.generateErrorMessage(t, o),
                            type: "error"
                        })
                    }
                }
                get generateRecoveryBody() {
                    return {
                        identifier: Ke[Te.getUserType],
                        identifierValue: Te.isLead ? tt.mobileNumber : tt.pan.toUpperCase()
                    }
                }
            }
            ;
            var rt = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class it extends pe {
                constructor() {
                    super(...arguments),
                    this.secretPin = "",
                    this.confirmedSecretPin = "",
                    this.confirmedSecretPinError = "",
                    this.setSecretPin = e=>{
                        this.secretPin = e
                    }
                    ,
                    this.setConfirmSecretPin = e=>{
                        this.confirmedSecretPin = e
                    }
                    ,
                    this.setConfirmedSecretPinError = e=>{
                        this.confirmedSecretPinError = e
                    }
                    ,
                    this.clearPinInfo = ()=>{
                        this.setSecretPin(""),
                        this.setConfirmSecretPin(""),
                        this.setConfirmedSecretPinError("")
                    }
                }
            }
            rt([s.observable], it.prototype, "secretPin", void 0),
            rt([s.observable], it.prototype, "confirmedSecretPin", void 0),
            rt([s.observable], it.prototype, "confirmedSecretPinError", void 0),
            rt([s.action], it.prototype, "setSecretPin", void 0),
            rt([s.action], it.prototype, "setConfirmSecretPin", void 0),
            rt([s.action], it.prototype, "setConfirmedSecretPinError", void 0);
            const nt = new it
              , st = {
                domain: "upstox.com",
                sameSite: "Strict"
            }
              , at = new class {
                constructor() {
                    this.setSecretPinRequest = async()=>{
                        const e = await Ue.request("2FA", "/2fa/secret-pin/set", "SET_PIN", {
                            method: "POST",
                            headers: Te.getPinRequestHeaders,
                            query: Te.pinRequestsQuery,
                            body: {
                                data: {
                                    newSecretPin: btoa(nt.secretPin),
                                    confirmNewSecretPin: btoa(nt.confirmedSecretPin)
                                }
                            }
                        });
                        await this.handlePinRequestsResponse(e)
                    }
                    ,
                    this.verifySecretePinRequest = async()=>{
                        var e, t;
                        const o = await Ue.request("2FA", "/2fa", "SET_PIN", {
                            method: "POST",
                            headers: Te.getPinRequestHeaders,
                            query: Te.pinRequestsQuery,
                            body: {
                                data: {
                                    twoFAMethod: "SECRET_PIN",
                                    inputText: btoa(nt.secretPin)
                                }
                            }
                        })
                          , r = no.getLoginSource()
                          , i = l.getItem("MOBILE_NUMBER");
                        o.success ? ($.sendEvent(V.LOGGED_IN, {
                            "User status": o.data.customerStatus,
                            "Profile ID": (null === (e = null == Te ? void 0 : Te.userProfile) || void 0 === e ? void 0 : e.profileId) || "",
                            "Login Step": "2FA",
                            "Phone number": Te.mobileNumber || i || "",
                            "User type": o.data.userType,
                            ...r && {
                                Source: r
                            }
                        }),
                        Te.isTradingViewApp && m.setItem("app_load_start_time", Date.now().toString(), st)) : $.sendEvent(V.LOGIN_FAILED, {
                            "User status": "REJECTED",
                            "Login Step": "2FA",
                            "Phone number": Te.mobileNumber || i || "",
                            "Login Failure Reason": `${o.error.message} [${o.error.code}]`,
                            "Login Failure Error Code": String(o.error.code),
                            "Profile ID": null === (t = null == Te ? void 0 : Te.userProfile) || void 0 === t ? void 0 : t.profileId,
                            ...r && {
                                Source: r
                            }
                        }),
                        await this.handlePinRequestsResponse(o, !0)
                    }
                    ,
                    this.forgotPinRequest = async e=>{
                        const t = await Ue.request("2FA", "/2fa/secret-pin/forgot/set-new-pin", "SET_PIN", {
                            method: "POST",
                            body: {
                                data: {
                                    forgotSecretPinToken: e,
                                    newSecretPin: btoa(nt.secretPin),
                                    confirmNewSecretPin: btoa(nt.secretPin)
                                }
                            }
                        });
                        t.success ? (X.push("/"),
                        nt.clearPinInfo(),
                        $.sendEvent(V.CHANGED_PIN, {
                            "User status": "APPROVED",
                            "Change PIN Step": "Pin Changed"
                        })) : this.pushErrorNotification(t.error.message, t.error.code)
                    }
                    ,
                    this.validateConfirmedPin = ()=>{
                        nt.secretPin !== nt.confirmedSecretPin && nt.setConfirmedSecretPinError("Does not fit secret pin")
                    }
                    ,
                    this.handlePinRequestsResponse = async(e,t=!1)=>{
                        var o;
                        if (e.success) {
                            const {isExternalClientOAuthApp: r, redirectUri: i, customerStatus: n} = e.data;
                            if (t && r && !i)
                                await no.startOauth();
                            else
                                switch (t || (null === (o = null === window || void 0 === window ? void 0 : window.dataLayer) || void 0 === o || o.push({
                                    event: "Enter_New_Pin"
                                }),
                                $.sendEvent(V.CHANGED_PIN, {
                                    "User status": "APPROVED",
                                    "Change PIN Step": "Pin Changed"
                                })),
                                m.setItem("customer_status", n, {
                                    domain: "upstox.com",
                                    sameSite: "Strict"
                                }),
                                m.removeItem("lead_phone_number"),
                                n) {
                                case "DORMANT":
                                case "INACTIVE":
                                    Z.goToRoute("/reactivate-account");
                                    break;
                                default:
                                    no.handleRedirect(i, !0)
                                }
                        } else
                            $.sendEvent(V.CHANGE_PIN_FAILED, {
                                "User status": "REJECTED",
                                "Change PIN Step": "Change Pin Button",
                                "Change PIN Failure Reason": e.error.message,
                                "Change PIN Error Code": String(e.error.code)
                            }),
                            1017007 === e.error.code ? (X.push("/"),
                            nt.clearPinInfo(),
                            this.pushErrorNotification(e.error.message, e.error.code)) : this.pushErrorNotification(e.error.message, e.error.code)
                    }
                    ,
                    this.pushErrorNotification = (e,t)=>{
                        L.pushNotificationWithOverlay({
                            key: "SET_PIN",
                            title: ke.generateErrorMessage(e, t),
                            type: "error"
                        })
                    }
                }
            }
              , ct = (0,
            n.Pi)((()=>{
                const {hasSecretPin: e} = A("AuthStore")
                  , {toggleModal: t} = A("AppStore");
                return e ? r.createElement(R.View, {
                    margin: [24, 0, 0, 0],
                    flex: !0,
                    justifyContent: "center"
                }, (()=>{
                    const e = l.getItem("MOBILE_NUMBER");
                    return e ? r.createElement(R.Text, {
                        variant: "body"
                    }, "Signed in as", " ", r.createElement(R.Text, {
                        variant: "bodyBold"
                    }, e), ".") : null
                }
                )(), r.createElement(R.Text, null, " "), r.createElement(R.Link, {
                    onClick: ()=>{
                        t("logoutModal")
                    }
                }, "Switch account?")) : null
            }
            ))
              , lt = ()=>({
                alignSelf: "end",
                cursor: "pointer"
            })
              , ut = e=>"ForgotPinStore" === e
              , dt = (0,
            n.Pi)((({stepControllerStoreKey: e, firstStepId: t})=>{
                const {hasSecretPin: o, userProfile: i, isLead: n, userFirstName: s} = A("AuthStore")
                  , {step: a} = A(e)
                  , c = null !== i && null !== i.firstName
                  , l = c && !n ? `Hi ${s}` : "Hi there!";
                return o && !ut(e) ? r.createElement(R.Text, {
                    transform: c && !n ? "capitalize" : "none",
                    variant: "heading2"
                }, l) : r.createElement(R.Text, {
                    variant: "heading2"
                }, a === t ? "Create a new 6-digit PIN" : "Confirm your PIN")
            }
            ))
              , pt = (0,
            n.Pi)((({stepControllerStoreKey: e, secondStepId: t})=>{
                const {hasSecretPin: o} = A("AuthStore")
                  , {step: i} = A(e);
                return r.createElement(R.Text, {
                    variant: "body"
                }, o && !ut(e) ? "Welcome back" : i === t ? "Enter the PIN again to set it up." : r.createElement(r.Fragment, null, r.createElement(R.Text, {
                    variant: "body"
                }, "This helps you access your account quickly and securely."), r.createElement(R.Text, null, " "), r.createElement(R.Link, {
                    onClick: ()=>{
                        Z.openInNewTab("https://help.upstox.com/support/solutions/folders/277003")
                    }
                }, "Learn more")))
            }
            ))
              , mt = (0,
            n.Pi)((()=>{
                const {profileDetails: e, isReturnedUser: t} = A("AuthStore");
                return t ? r.createElement(R.Avatar, {
                    name: e.fullName,
                    image: e.avatar ? e.avatar : void 0
                }) : null
            }
            ))
              , ht = (0,
            n.Pi)((({formType: e, stepControllerStoreKey: t, firstStepId: o, secondStepId: i})=>{
                const {clearPinInfo: n, setSecretPin: s, setConfirmSecretPin: a, confirmedSecretPin: c, secretPin: l, confirmedSecretPinError: u, setConfirmedSecretPinError: d} = A("SecretPinStore")
                  , {step: p, goStepForward: m} = A(t)
                  , {hasSecretPin: h, otpTo2FATime: g, setOtpTo2FATime: f, isQRLoginEnabled: v} = A("AuthStore")
                  , {verifyOtpToken: E} = A("OtpStore")
                  , y = no.getLoginSource()
                  , {setStep: b, setPreviousStep: T, setPAN: P, setMobileNumber: w} = A("ForgotPinStore")
                  , {loadings: {SET_PIN: I}} = A("LoadingStore")
                  , {server: {SET_PIN: x}, clearErrorByKey: O} = A("ErrorStore");
                (0,
                r.useEffect)((()=>{
                    if (g) {
                        const e = Date.now() - g;
                        $.sendEvent(V.OTP_TO_2FA_TIME, {
                            "Time taken": `${e} ms`,
                            ...y && {
                                Source: y
                            }
                        }),
                        f(0)
                    }
                }
                ), []),
                (0,
                r.useEffect)((()=>{
                    n(),
                    no.checkAuthIdentityTokenExpiry()
                }
                ), [n]),
                (0,
                r.useEffect)((()=>()=>{
                    O("SET_PIN")
                }
                ), [O]);
                const S = ()=>{
                    b(0),
                    T(0),
                    P(""),
                    w("")
                }
                  , C = ()=>{
                    S(),
                    Z.goToRoute("/forgot-pin")
                }
                  , k = 1017090 === (null == x ? void 0 : x.code)
                  , _ = v && h && !ut(t);
                return r.createElement(Et, {
                    title: v ? null : r.createElement(dt, {
                        stepControllerStoreKey: t,
                        firstStepId: o
                    }),
                    avatar: ut(t) || !h ? void 0 : r.createElement(mt, null),
                    subtitle: v ? null : r.createElement(pt, {
                        stepControllerStoreKey: t,
                        secondStepId: i
                    }),
                    stepControllerStoreKey: t,
                    rightIcon: h && !ut(t) && r.createElement(R.Button, {
                        variant: "invisible",
                        onClick: C
                    }, r.createElement(R.Text, {
                        variant: "bodyBold",
                        color: "text.link"
                    }, "Forgot PIN?")),
                    footer: "AuthStore" === t && !v && r.createElement(ct, null)
                }, r.createElement(R.View, {
                    as: "form",
                    id: "secret-pin-form",
                    flex: !0,
                    flexDirection: "column",
                    justifyContent: "space-between",
                    onSubmit: t=>{
                        switch (t.preventDefault(),
                        e) {
                        case "createPin":
                            p === o ? m(i) : at.setSecretPinRequest();
                            break;
                        case "enterPin":
                            k ? (S(),
                            Z.goToRoute("/unlock-account")) : at.verifySecretePinRequest();
                            break;
                        case "forgotPin":
                            at.forgotPinRequest(E);
                            break;
                        default:
                            m(i)
                        }
                    }
                    ,
                    padding: [0, 0, 20]
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    padding: [0, 16],
                    margin: [0, 0, 20]
                }, r.createElement(bt, {
                    onChange: ({target: e})=>{
                        const t = e.value.trim()
                          , r = Number.isNaN(Number(t)) ? l : t;
                        p === o ? s(r) : (d(""),
                        a(r))
                    }
                    ,
                    value: p === o ? l : c,
                    isLogin: h && !ut(t),
                    error: u,
                    disabled: k,
                    isFirstScreen: p === o
                }), _ && r.createElement(R.View, {
                    as: "a",
                    onClick: C,
                    css: lt
                }, r.createElement(R.Text, {
                    variant: "bodyBold",
                    color: "text.link"
                }, "Forgot PIN?")), k && r.createElement(R.View, {
                    margin: [16, 0, 0]
                }, r.createElement(R.Alert, {
                    variant: "warning",
                    width: "inline",
                    cardVariant: "primary",
                    icon: r.createElement(R.LockClosedIcon, {
                        size: "large"
                    }),
                    title: r.createElement(R.Text, {
                        variant: "meta",
                        lineHeight: "meta"
                    }, "Due to too many incorrect PIN attempts, your account has been locked. Unlock your account by verifying your details.")
                }))), r.createElement(R.Button, {
                    disabled: p === o ? !l.length : !c.length || !!u,
                    width: "full",
                    type: "submit",
                    isLoading: I,
                    id: "pinContinueBtn"
                }, k ? "Unlock account" : "Continue")))
            }
            ))
              , gt = ()=>({
                width: "100%",
                height: "100%"
            })
              , ft = ({theme: e, cssProps: {isMobile: t, isQRLoginEnabled: o}})=>({
                background: (0,
                R.color)(e, "background.default"),
                width: "100%",
                height: "100%",
                ...!t && !o && {
                    maxWidth: 448,
                    minWidth: 320,
                    height: "auto",
                    borderRadius: 8
                }
            })
              , vt = ({cssProps: {isMobile: e}})=>({
                width: "100%",
                ...!e && {
                    maxWidth: 340
                }
            })
              , Et = (0,
            n.Pi)((({title: e, subtitle: t, rightIcon: o, stepControllerStoreKey: i, children: n, avatar: s, footer: a})=>{
                const {step: c, goStepBack: l} = A(i)
                  , {isQRLoginEnabled: u} = A("AuthStore")
                  , {isMobile: d} = A("PlatformStore")
                  , p = u && !("ForgotPinStore" === i);
                return r.createElement(R.View, {
                    flexDirection: "column",
                    alignItems: "center",
                    css: gt,
                    cssProps: {
                        isMobile: d
                    }
                }, r.createElement(R.View, {
                    justifyContent: "flex-start",
                    flexDirection: "column",
                    css: ft,
                    cssProps: {
                        isMobile: d,
                        isQRLoginEnabled: p
                    }
                }, !p && r.createElement(R.View, {
                    justifyContent: c ? "space-between" : "flex-end",
                    padding: 16,
                    inline: !0
                }, r.createElement(R.View, null, 0 === c || s ? s : r.createElement(R.ArrowLeftIcon, {
                    cursor: "pointer",
                    onClick: l,
                    size: "large"
                })), o || r.createElement(R.ButtonIcon, {
                    as: "a",
                    variant: "invisible",
                    href: te,
                    target: "_blank"
                }, r.createElement(R.SupportCircleIcon, {
                    color: "text.metaBold",
                    size: "large"
                }))), r.createElement(R.View, {
                    flexDirection: "column",
                    gap: 8,
                    padding: p ? [0, 48, 20, 20] : [0, 32, 32]
                }, e, t), r.createElement(R.View, {
                    flex: !0,
                    padding: p ? [0, 48, 0, 4] : [0, 16, 16]
                }, n)), a && r.createElement(R.View, {
                    css: vt
                }, a))
            }
            ))
              , yt = ()=>({
                width: "100%"
            })
              , bt = ({value: e, onChange: t, disabled: o, isLogin: i, error: n, isFirstScreen: s})=>{
                const a = s ? "Create a new 6-digit PIN" : "Verify your 6-digit PIN";
                return r.createElement(R.InputField, {
                    id: "pinCode",
                    required: !0,
                    label: i ? "Enter 6-digit PIN" : a,
                    variant: "secondary",
                    value: e,
                    type: "password",
                    inputMode: "numeric",
                    disabled: o,
                    error: n,
                    css: yt,
                    InputProps: {
                        onChange: t,
                        maxLength: 6,
                        autoFocus: !0
                    }
                })
            }
              , Tt = (0,
            n.Pi)((({children: e})=>{
                const {loadings: {VERIFY_IDENTITY_TOKEN: t, LOGOUT: o}} = A("LoadingStore")
                  , {pathname: i} = (0,
                S.TH)();
                return (0,
                r.useEffect)((()=>{
                    "/logout" === i || o || no.checkIdentityToken()
                }
                ), [o, i]),
                t ? r.createElement(fr, null) : e
            }
            ))
              , Pt = (0,
            n.Pi)((()=>{
                const {toggleModal: e, modalsConfig: {logoutModal: t}} = A("AppStore")
                  , {loadings: {LOGOUT: o}} = A("LoadingStore");
                return t ? r.createElement(Er, {
                    footer: r.createElement(R.View, {
                        flexDirection: "row",
                        justifyContent: "space-between",
                        gap: "medium"
                    }, r.createElement(R.Button, {
                        width: "full",
                        onClick: ()=>{
                            e("logoutModal")
                        }
                        ,
                        variant: "secondary"
                    }, "Cancel"), r.createElement(R.Button, {
                        width: "full",
                        onClick: ()=>no.logoutRequest(),
                        isLoading: o
                    }, "Switch"))
                }, r.createElement(R.View, {
                    flexDirection: "column",
                    justifyContent: "center",
                    flex: !0
                }, r.createElement(R.Text, {
                    variant: "meta",
                    size: "m",
                    align: "center"
                }, "Are you sure you want to switch your account?"))) : null
            }
            ))
              , wt = ()=>({
                width: "100%"
            })
              , It = (0,
            n.Pi)((({storeKey: e="AuthStore", buttonStyles: t})=>{
                const {setMobileNumber: o, mobileNumber: i} = A(e)
                  , {setLoginTo1FATime: n, isQRLoginEnabled: s} = A("AuthStore")
                  , {loadings: {"1FA_OTP_GENERATE": a, FORGOT_PIN_OTP: c}} = A("LoadingStore")
                  , l = s && !("ForgotPinStore" === e)
                  , u = (0,
                r.useMemo)((()=>c || a), [c, a])
                  , d = (0,
                r.useMemo)((()=>!Ye.isIndiaPhoneNumber(i)), [i]);
                return r.createElement(R.View, {
                    as: "form",
                    id: "mobile-number-form",
                    flex: !0,
                    flexDirection: "column",
                    justifyContent: "space-between",
                    onSubmit: t=>{
                        t.preventDefault(),
                        "AuthStore" === e ? (no.generateOtpRequest(),
                        n(Date.now())) : ot.generateOtpRequest()
                    }
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    padding: l ? [0, 0, 12] : [0, 0, 20]
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    padding: [0, 16],
                    margin: [0, 0, 20]
                }, r.createElement(R.InputField, {
                    label: "Enter mobile number",
                    variant: "secondary",
                    value: i.trim(),
                    disabled: u,
                    InputProps: {
                        onChange: ({target: {value: e}})=>{
                            !Number.isNaN(Number(e)) && e.length <= 10 && o(e)
                        }
                        ,
                        maxLength: 10,
                        autoFocus: !0,
                        id: "mobileNum"
                    },
                    error: ke.mobileNumberValidationMessage(d, String(i)),
                    before: r.createElement(R.Text, {
                        variant: "body",
                        color: "text.2"
                    }, "+", 91),
                    css: wt
                })), r.createElement(R.Button, {
                    disabled: d,
                    width: "full",
                    style: t,
                    type: "submit",
                    isLoading: u,
                    id: "getOtp"
                }, "Get OTP")))
            }
            ))
              , xt = o.p + "assets/stars.svg"
              , Ot = ()=>({
                display: "flex",
                width: "100%",
                boxShadow: "inset 0px -1px 0px #E1E1E1",
                padding: "0px 24px 8px",
                marginBottom: 8
            })
              , St = ()=>({
                display: "flex",
                width: "100%"
            })
              , At = ({theme: e})=>({
                display: "flex",
                flexDirection: "column",
                background: (0,
                R.color)(e, "background.default"),
                borderRadius: 8,
                padding: 24
            })
              , Rt = ()=>({
                width: 420,
                padding: "8px 8px 0px"
            })
              , Ct = ()=>({
                width: 420,
                padding: "8px 8px 0px",
                borderLeft: "1px solid #F2F2F2"
            })
              , kt = ()=>({
                alignSelf: "end"
            })
              , _t = ()=>({
                display: "flex",
                alignItems: "center",
                position: "absolute",
                cursor: "pointer",
                right: 0,
                top: 0
            })
              , Nt = {
                maxWidth: 324,
                margin: "0 auto"
            }
              , Dt = ({isMobile: e, isTotpLoginEnabled: t})=>e || t ? null : r.createElement(R.View, {
                css: _t,
                onClick: ()=>{
                    try {
                        $.sendEvent(V.TRY_TOTP, {})
                    } catch (e) {}
                    Z.openInNewTab("https://help.upstox.com/support/solutions/articles/260346-what-is-totp-how-to-enable-totp-through-desktop-")
                }
            }, r.createElement("img", {
                src: xt,
                height: 16,
                width: 16,
                alt: "Stars"
            }), r.createElement(R.Text, {
                color: "text.link",
                weight: "bold"
            }, "Try TOTP?"))
              , Lt = (0,
            n.Pi)((()=>{
                const {referralBody: e, loginTo1FATime: t, setLoginTo1FATime: o, isQRLoginEnabled: i, isTotpLoginEnabled: n} = A("AuthStore")
                  , {infoMessage: s} = A("OtpStore")
                  , {isMobile: a} = A("PlatformStore")
                  , c = no.getLoginSource();
                return (0,
                r.useEffect)((()=>{
                    if (t) {
                        const e = Date.now() - t;
                        $.sendEvent(V.LOGIN_TO_1FA_TIME, {
                            "Time taken": `${e} ms`,
                            ...c && {
                                Source: c
                            }
                        }),
                        o(0)
                    }
                }
                ), []),
                r.createElement(Et, {
                    stepControllerStoreKey: "AuthStore",
                    title: r.createElement(R.Text, {
                        variant: i ? "heading3" : "heading2",
                        weight: i ? "bold" : "heading2"
                    }, "Verify your number"),
                    subtitle: r.createElement(R.Text, {
                        variant: i ? "meta" : "body"
                    }, s || We),
                    rightIcon: r.createElement(Je, {
                        resendOtpRequest: no.generateOtpRequest
                    })
                }, r.createElement(ze, {
                    otpConfigKey: "1FA_OTP",
                    onOtpVerifiedCallback: no.handleValidateOtpResponse,
                    additionalData: e,
                    tryTotpInfo: r.createElement(Dt, {
                        isMobile: a,
                        isTotpLoginEnabled: n
                    }),
                    bottomIcon: i ? r.createElement(R.View, {
                        css: kt
                    }, r.createElement(Je, {
                        resendOtpRequest: no.generateOtpRequest
                    })) : null
                }))
            }
            ))
              , Vt = o.p + "assets/people.svg"
              , Ut = o.p + "assets/qr.svg";
            var qt = o(84059);
            const Ft = o.p + "assets/upstox-logo-small.svg";
            var Mt = o(48764);
            const Bt = new class {
                constructor() {
                    this.loggerEnabled = w,
                    this.error = (...e)=>{
                        this.loggerEnabled && console.error(...e)
                    }
                    ,
                    this.log = (e,...t)=>{
                        this.loggerEnabled && console.log(`>>> ${e}:`, ...t)
                    }
                }
            }
              , Wt = e=>{
                const [t,o] = (0,
                r.useState)({
                    ...ve,
                    loading: !0
                })
                  , {SOCKET_SERVER_URL: i, clientId: n, redirectUri: s} = e
                  , a = (0,
                r.useRef)(Ee)
                  , c = (0,
                r.useRef)(null)
                  , l = (0,
                r.useRef)()
                  , u = (0,
                r.useRef)(null)
                  , d = (0,
                r.useRef)(!1)
                  , p = (0,
                r.useRef)(null);
                return (0,
                r.useEffect)((()=>{
                    function e() {
                        const {osName: e, osVersion: t, browserName: o, manufacturer: r} = ge.getDeviceDetails();
                        return `platform=WEB|osName=${e}|osVersion=${t}|appVersion=4.0.0|modelName=${o}|manufacturer=${r}`
                    }
                    function t(e) {
                        var t, r, i, n, s, l;
                        if (Bt.log("WS", e),
                        (null === (t = null == e ? void 0 : e.data) || void 0 === t ? void 0 : t.isQrLoginAccepted) && (null === (r = null == e ? void 0 : e.data) || void 0 === r ? void 0 : r.autoLoginToken))
                            c.current && c.current.close(),
                            no.autoLoginQRRequest(e.data.autoLoginToken),
                            o({
                                ...ve,
                                success: !0
                            });
                        else if (null === (i = null == e ? void 0 : e.data) || void 0 === i ? void 0 : i.qrCode) {
                            const t = (null === (n = e.data.qrCode) || void 0 === n ? void 0 : n.content) || "";
                            a.current = {
                                validityInSeconds: (null === (l = null === (s = e.data) || void 0 === s ? void 0 : s.qrCode) || void 0 === l ? void 0 : l.validityInSeconds) || Ee.validityInSeconds,
                                qrCodeAutoRefreshPendingCount: a.current.qrCodeAutoRefreshPendingCount
                            },
                            o({
                                ...ve,
                                qrContent: t
                            })
                        }
                    }
                    function r() {
                        v(),
                        d.current = !1
                    }
                    function m() {
                        c.current && (c.current.close(),
                        c.current = null)
                    }
                    const h = e=>{
                        u.current && clearTimeout(u.current),
                        e || d.current || (o((e=>e.error || e.success ? e : {
                            ...ve,
                            reloadQr: !0
                        })),
                        c.current = null)
                    }
                      , g = ()=>{
                        o({
                            ...ve,
                            error: !0
                        })
                    }
                    ;
                    function f() {
                        p.current && clearTimeout(p.current),
                        m(),
                        d.current = !0,
                        c.current = new class {
                            constructor(e, t, o, r, i) {
                                this.socket = null,
                                this.responseTimer = null,
                                this.socketUrl = "",
                                this.reconnectionTries = 3,
                                this.socketUrl = e,
                                this.responseHandler = t,
                                this.onSocketClose = r,
                                this.onConnection = o,
                                this.onSocketError = i,
                                this.connect()
                            }
                            connect() {
                                Bt.log("WS", "CONNECTING TO SOCKET");
                                const e = new WebSocket(this.socketUrl);
                                e.binaryType = "arraybuffer",
                                e.onopen = ()=>{
                                    this.socket = e,
                                    this.onConnection()
                                }
                                ,
                                e.onmessage = e=>{
                                    try {
                                        if (null == e ? void 0 : e.data) {
                                            this.clearResponseTimer();
                                            const t = Mt.lW.from(null == e ? void 0 : e.data);
                                            this.responseHandler(JSON.parse(null == t ? void 0 : t.toString()))
                                        }
                                    } catch (e) {}
                                }
                                ,
                                e.onclose = ()=>{
                                    Bt.log("WS", "SOCKET CONNECTION CLOSED"),
                                    this.socket = null;
                                    let e = !0;
                                    this.responseTimer && (this.clearResponseTimer(),
                                    this.reconnectionTries > 0 && (this.onSocketClose && this.onSocketClose(!0),
                                    this.connect(),
                                    this.reconnectionTries -= 1,
                                    e = !1)),
                                    e && this.onSocketClose && this.onSocketClose()
                                }
                                ,
                                e.onerror = e=>{
                                    Bt.log("WS", "ERROR SOCKET", e),
                                    this.onSocketError && this.onSocketError(JSON.stringify(e))
                                }
                            }
                            sendEvent(e) {
                                var t;
                                return Bt.log("WS", `${JSON.stringify(e)}, ${null === (t = this.socket) || void 0 === t ? void 0 : t.readyState}`),
                                !(!this.socket || 1 !== this.socket.readyState || (this.socket.send(Mt.lW.from(JSON.stringify(e))),
                                this.responseTimer = setTimeout((()=>{
                                    this.close(!1)
                                }
                                ), 3e3),
                                0))
                            }
                            clearResponseTimer() {
                                this.responseTimer && clearTimeout(this.responseTimer),
                                this.responseTimer = null
                            }
                            close(e=!0) {
                                e && this.clearResponseTimer(),
                                this.socket && 1 === this.socket.readyState && this.socket.close()
                            }
                        }
                        (i,t,r,h,g)
                    }
                    function v() {
                        if (u.current && clearTimeout(u.current),
                        !(a.current.qrCodeAutoRefreshPendingCount > 0))
                            return o({
                                ...ve,
                                reloadQr: !0
                            }),
                            void (p.current = setTimeout((()=>{
                                m()
                            }
                            ), 2e5));
                        if (u.current = setTimeout((()=>{
                            v()
                        }
                        ), 1e3 * a.current.validityInSeconds),
                        c.current) {
                            const t = {
                                requestId: ke.generateUniqueId(),
                                method: "GENERATE_LOGIN_QR_CODE",
                                clientId: n,
                                redirectUri: s,
                                deviceDetails: e()
                            };
                            c.current.sendEvent(t) && (a.current = {
                                validityInSeconds: a.current.validityInSeconds,
                                qrCodeAutoRefreshPendingCount: a.current.qrCodeAutoRefreshPendingCount - 1
                            },
                            Bt.log("WS", new Date),
                            o({
                                ...ve,
                                loading: !0
                            }))
                        }
                    }
                    l.current = function() {
                        o({
                            ...ve,
                            loading: !0
                        }),
                        f(),
                        a.current = {
                            validityInSeconds: Ee.validityInSeconds,
                            qrCodeAutoRefreshPendingCount: Ee.qrCodeAutoRefreshPendingCount
                        }
                    }
                    ,
                    i && s && n && f()
                }
                ), [i, s, n]),
                (0,
                r.useEffect)((()=>{
                    const e = ()=>{
                        !(null === navigator || void 0 === navigator ? void 0 : navigator.onLine) && c.current ? (c.current.close(),
                        o({
                            ...ve,
                            error: !0
                        }),
                        L.pushNotificationWithOverlay({
                            key: "DEACTIVATION_VALIDATE",
                            title: "Network Error. Try re-loading the page",
                            type: "error"
                        })) : c.current || o({
                            ...ve,
                            reloadQr: !0
                        }),
                        u.current && clearTimeout(u.current)
                    }
                    ;
                    return window.addEventListener("offline", e),
                    window.addEventListener("online", e),
                    ()=>{
                        window.removeEventListener("offline", e),
                        window.removeEventListener("online", e)
                    }
                }
                ), []),
                {
                    qrStatus: t,
                    reloadQr: l.current
                }
            }
              , jt = ()=>({
                width: "100%",
                height: "100%"
            })
              , Qt = ()=>({
                width: "100%",
                height: "100%",
                padding: "0 52px"
            })
              , Gt = ()=>({
                marginTop: "20px",
                justifyContent: "center"
            })
              , zt = {
                display: "flex"
            }
              , $t = {
                margin: "0 auto"
            }
              , Ht = ()=>({
                position: "relative"
            })
              , Kt = ()=>({
                width: 56,
                height: 56,
                borderRadius: "50%",
                background: "#5A298B",
                display: "flex",
                justifyContent: "center",
                cursor: "pointer",
                alignItems: "center"
            })
              , Yt = ({cssProps: {status: e}})=>({
                position: "absolute",
                cursor: "loadQr" === e ? "pointer" : "default",
                top: "50%",
                left: "50%",
                transform: "translate(-50%, -50%)"
            })
              , Xt = (0,
            n.Pi)((()=>{
                const {clientId: e, redirectUrl: t} = A("AuthStore")
                  , {qrStatus: o, reloadQr: i} = Wt({
                    SOCKET_SERVER_URL: x[P],
                    clientId: e,
                    redirectUri: t
                })
                  , n = (0,
                r.useCallback)((e=>e.loading ? r.createElement(R.Loading, null) : e.success ? r.createElement(R.CheckboxCheckedIcon, {
                    size: "xxlarge",
                    color: "background.green"
                }) : e.error ? r.createElement(R.ErrorCircleIcon, {
                    size: "xxlarge",
                    color: "background.orange"
                }) : e.reloadQr ? r.createElement(R.View, {
                    css: Kt
                }, r.createElement(R.LoadMoreIcon, {
                    size: "large",
                    color: "background.default"
                })) : null), [])
                  , s = (0,
                r.useMemo)((()=>({
                    size: "136px",
                    opacity: o.qrContent ? 1 : .2
                })), [o])
                  , a = (0,
                r.useCallback)((()=>{
                    o.reloadQr && i && i()
                }
                ), [o, i]);
                return r.createElement(R.View, {
                    css: Gt
                }, r.createElement(R.View, {
                    css: Ht
                }, r.createElement(qt.Qd, {
                    value: o.qrContent || "",
                    style: s,
                    imageSettings: {
                        src: Ft,
                        x: void 0,
                        y: void 0,
                        height: 24,
                        width: 24,
                        excavate: !1
                    }
                }), !o.qrContent && r.createElement(R.View, {
                    css: Yt,
                    cssProps: {
                        qrStatus: o
                    },
                    onClick: a
                }, n(o))))
            }
            ))
              , Jt = (0,
            n.Pi)((()=>{
                const {isMobile: e} = A("PlatformStore");
                return r.createElement(R.View, {
                    flexDirection: "column",
                    alignItems: "center",
                    css: jt,
                    cssProps: {
                        isMobile: e
                    }
                }, r.createElement(R.View, {
                    justifyContent: "flex-start",
                    flexDirection: "column",
                    css: Qt
                }, r.createElement(R.View, {
                    flexDirection: "column",
                    gap: 8
                }, r.createElement(R.Text, {
                    color: "text.1",
                    weight: "bold",
                    size: "m"
                }, "Login with QR code"), r.createElement(R.Text, {
                    size: "s",
                    color: "text.2"
                }, "Scan this code with your Upstox mobile app and log in instantly")), r.createElement(R.View, {
                    flexDirection: "column",
                    margin: [8, 0, 0],
                    as: "ol"
                }, r.createElement("li", null, r.createElement(R.Text, {
                    size: "s",
                    color: "text.2",
                    style: zt
                }, "1. Go to Accounts ", r.createElement("img", {
                    src: Vt,
                    alt: "grow img",
                    style: $t
                }), " > Select ", r.createElement("img", {
                    src: Ut,
                    alt: "grow img",
                    style: $t
                }), " scan icon from top bar")), r.createElement("li", null, r.createElement(R.Text, {
                    size: "s",
                    color: "text.2"
                }, "2. Point your phone at this screen to confirm login"))), r.createElement(Xt, null)))
            }
            ))
              , Zt = (0,
            n.Pi)((()=>{
                const {profileDetails: e, isReturnedUser: t} = A("AuthStore")
                  , o = {
                    name: e.fullName
                };
                return e.avatar && (o.image = e.avatar),
                t ? r.createElement(R.Avatar, {
                    ...o
                }) : null
            }
            ))
              , eo = (0,
            n.Pi)((({stepControllerStoreKey: e, firstStepId: t})=>{
                const {hasSecretPin: o, userProfile: i, isLead: n, userFirstName: s} = A("AuthStore")
                  , {step: a} = A(e)
                  , c = null !== i && null !== i.firstName
                  , l = c && !n ? `Hi ${s}` : "Hi there!";
                return o && "ForgotPinStore" !== e ? r.createElement(R.View, {
                    alignItems: "center",
                    gap: 16
                }, r.createElement(Zt, null), r.createElement(R.Text, {
                    transform: c && !n ? "capitalize" : "none",
                    variant: "heading2"
                }, l)) : r.createElement(R.Text, {
                    variant: "heading2"
                }, a === t ? "Create a new 6-digit PIN" : "Confirm your PIN")
            }
            ))
              , to = (0,
            n.Pi)((()=>{
                const {step: e, qrConfig: t, goStepBack: o, setMobileNumber: i, hasSecretPin: n, isQRLoginEnabled: s, setQrLoginEnabled: a} = A("AuthStore")
                  , {loadings: {REMOTE_CONFIG: c}} = A("LoadingStore");
                (0,
                r.useEffect)((()=>{
                    var e, o;
                    void 0 === (null === (e = null == t ? void 0 : t.qrLogin) || void 0 === e ? void 0 : e.enabled) ? no.remoteConfig() : a(!!(null === (o = null == t ? void 0 : t.qrLogin) || void 0 === o ? void 0 : o.enabled))
                }
                ), [t, a]),
                (0,
                r.useEffect)((()=>()=>{
                    i("")
                }
                ), [i]);
                const l = ()=>{
                    switch (e) {
                    case 1:
                        return r.createElement(Lt, null);
                    case 2:
                    case 3:
                        return r.createElement(ht, {
                            formType: n ? "enterPin" : "createPin",
                            stepControllerStoreKey: "AuthStore",
                            firstStepId: 2,
                            secondStepId: 3
                        });
                    default:
                        return r.createElement(Et, {
                            stepControllerStoreKey: "AuthStore",
                            title: r.createElement(R.Text, {
                                variant: s ? "heading3" : "heading2",
                                weight: "bold",
                                color: "text.1"
                            }, s ? "Login with mobile number" : fe),
                            subtitle: r.createElement(R.Text, {
                                variant: "body",
                                color: "text.2",
                                size: s ? "s" : "body"
                            }, "We’ll send you a one-time password (OTP) to verify your mobile number.")
                        }, r.createElement(It, {
                            storeKey: "AuthStore",
                            buttonStyles: s ? Nt : {}
                        }))
                    }
                }
                ;
                return c ? r.createElement(fr, null) : s ? r.createElement(R.View, {
                    flexDirection: "column"
                }, r.createElement(R.View, {
                    css: At
                }, r.createElement(R.View, {
                    css: Ot
                }, (()=>{
                    switch (e) {
                    case 1:
                        return r.createElement(R.View, {
                            css: St,
                            justifyContent: "space-between"
                        }, r.createElement(R.View, {
                            alignItems: "center"
                        }, r.createElement(R.ArrowLeftIcon, {
                            cursor: "pointer",
                            onClick: o,
                            size: "large"
                        })), r.createElement(R.View, {
                            justifyContent: "flex-end",
                            inline: !0
                        }, r.createElement(R.ButtonIcon, {
                            as: "a",
                            variant: "invisible",
                            href: te,
                            target: "_blank"
                        }, r.createElement(R.SupportCircleIcon, {
                            color: "text.metaBold",
                            size: "large"
                        }))));
                    case 2:
                        return r.createElement(R.View, {
                            css: St,
                            justifyContent: "space-between"
                        }, r.createElement(R.View, null), r.createElement(eo, {
                            stepControllerStoreKey: "AuthStore",
                            firstStepId: 2
                        }), r.createElement(R.View, {
                            justifyContent: "flex-end",
                            inline: !0
                        }, r.createElement(R.ButtonIcon, {
                            as: "a",
                            variant: "invisible",
                            href: te,
                            target: "_blank"
                        }, r.createElement(R.SupportCircleIcon, {
                            color: "text.metaBold",
                            size: "large"
                        }))));
                    default:
                        return r.createElement(R.View, {
                            css: St,
                            justifyContent: "space-between"
                        }, r.createElement(R.View, null), r.createElement(R.View, {
                            flexDirection: "column"
                        }, r.createElement(R.Text, {
                            variant: "heading2",
                            color: "text.1"
                        }, fe)), r.createElement(R.View, {
                            justifyContent: "flex-end",
                            inline: !0
                        }, r.createElement(R.ButtonIcon, {
                            as: "a",
                            variant: "invisible",
                            href: te,
                            target: "_blank"
                        }, r.createElement(R.SupportCircleIcon, {
                            color: "text.metaBold",
                            size: "large"
                        }))))
                    }
                }
                )()), r.createElement(R.View, null, r.createElement(R.View, {
                    css: Rt
                }, l()), r.createElement(R.View, {
                    css: Ct
                }, r.createElement(Jt, null)))), (2 === e || 3 === e) && r.createElement(ct, null)) : r.createElement(r.Fragment, null, l())
            }
            ))
              , oo = ()=>({
                width: "100%"
            })
              , ro = (0,
            n.Pi)((()=>{
                const {pan: e, setPAN: t} = A("ForgotPinStore")
                  , {loadings: {FORGOT_PIN_OTP: o}} = A("LoadingStore");
                return r.createElement(R.View, {
                    as: "form",
                    id: "pan-form",
                    flex: !0,
                    flexDirection: "column",
                    justifyContent: "space-between",
                    onSubmit: e=>{
                        e.preventDefault(),
                        ot.generateOtpRequest()
                    }
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    padding: [0, 0, 20]
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    padding: [0, 16],
                    margin: [0, 0, 20]
                }, r.createElement(R.InputField, {
                    label: "Enter your PAN",
                    variant: "secondary",
                    value: e.toUpperCase().trim(),
                    InputProps: {
                        onChange: ({target: {value: e}})=>{
                            t(e)
                        }
                        ,
                        autoFocus: !0
                    },
                    css: oo
                })), r.createElement(R.Button, {
                    disabled: !Ye.isPANCard(e),
                    width: "full",
                    type: "submit",
                    isLoading: o
                }, "Continue")))
            }
            ))
              , io = (0,
            n.Pi)((()=>{
                const {step: e, goStepForward: t, setPreviousStep: o} = A("ForgotPinStore")
                  , {isLead: i} = A("AuthStore")
                  , {infoMessage: n} = A("OtpStore")
                  , s = ()=>{
                    o(e),
                    t(3)
                }
                ;
                switch (e) {
                case 1:
                    return r.createElement(Et, {
                        stepControllerStoreKey: "ForgotPinStore",
                        title: r.createElement(R.Text, {
                            variant: "heading2"
                        }, "Verify your number"),
                        subtitle: r.createElement(R.Text, null, n || We),
                        rightIcon: r.createElement(Je, {
                            resendOtpRequest: ot.generateOtpRequest
                        })
                    }, r.createElement(ze, {
                        otpConfigKey: "FORGOT_PIN_OTP",
                        onOtpVerifiedCallback: s
                    }));
                case 2:
                case 3:
                    return r.createElement(ht, {
                        formType: "forgotPin",
                        stepControllerStoreKey: "ForgotPinStore",
                        firstStepId: 2,
                        secondStepId: 3
                    });
                default:
                    return r.createElement(Et, {
                        stepControllerStoreKey: "ForgotPinStore",
                        title: r.createElement(R.Text, {
                            variant: "heading2",
                            color: "text.1"
                        }, "Forgot PIN"),
                        subtitle: r.createElement(R.Text, {
                            variant: "body",
                            color: "text.2"
                        }, i ? "To set a new PIN, you’ll get a one-time password (OTP) on your mobile number." : "To keep your account secure, we need to verify it’s you.")
                    }, i ? r.createElement(It, {
                        storeKey: "ForgotPinStore"
                    }) : r.createElement(ro, null))
                }
            }
            ))
              , no = new class {
                constructor() {
                    this.stepReaction = (0,
                    s.reaction)((()=>Te.step), (e=>{
                        e === Te.previousStep && 0 !== e && this.generateOtpRequest(!1, !0)
                    }
                    )),
                    this.logout = ()=>{
                        this.logoutRequest(!0),
                        Z.goToRoute("/", {
                            query: {
                                redirect_uri: Te.redirectUrl,
                                client_id: Te.clientId,
                                platform_id: Te.platformId,
                                redirect_path: Te.redirectPath,
                                redirect_query: Te.redirectQuery
                            }
                        })
                    }
                    ,
                    this.logoutRequest = async(e=!1)=>{
                        try {
                            await Ue.request("LOGOUT", "/logout", "LOGOUT", {
                                method: "POST"
                            })
                        } catch (e) {
                            L.pushNotificationWithOverlay({
                                key: "LOGOUT",
                                title: "Unable to logout",
                                type: "error"
                            })
                        } finally {
                            Te.reset(),
                            this.checkIdentityToken(),
                            e || b.toggleModal("logoutModal")
                        }
                    }
                    ,
                    this.checkIdentityToken = ()=>{
                        l.getItem("AUTH_IDENTITY_SET") && !Te.isRedirecting ? this.checkMobileNumberCookie() ? Te.setStep(1) : "CUSTOMER" === Te.userType ? Te.setStep(2) : this.checkLeadToken() : this.checkMobileNumberCookie() || Te.setStep(0)
                    }
                    ,
                    this.checkAuthIdentityTokenExpiry = ()=>{
                        const e = m.getItem("auth_identity_token_expiry");
                        let t = !0;
                        e && (t = we()(Number(e)).isBefore(we()())),
                        t && (Te.reset(),
                        Z.goToRoute("/"))
                    }
                    ,
                    this.generateOtpRequest = async(e=!1,t=!1)=>{
                        var o, r;
                        const i = await Ue.request("1FA_OTP", "/v5/auth/1fa/otp/generate", "1FA_OTP_GENERATE", {
                            method: "POST",
                            body: {
                                data: {
                                    mobileNumber: Te.mobileNumber
                                }
                            }
                        });
                        if (i.success)
                            Me.setVerifyOtpToken(i.data.validateOTPToken),
                            Me.setInfoMessage(i.data.message),
                            Te.setOtpRequestInterval(i.data.nextRequestInterval),
                            Te.setTotpLoginEnabled(!!(null === (o = i.data) || void 0 === o ? void 0 : o.isTotpEnabled)),
                            e ? L.pushNotificationWithOverlay({
                                key: "OTP_RESEND",
                                type: "success",
                                title: "OTP has been resent to your Phone!"
                            }) : (L.pushNotificationWithOverlay({
                                key: "OTP_SEND",
                                type: "success",
                                title: "OTP has been sent to your Phone!"
                            }),
                            t || Te.goStepForward(1),
                            X.location.pathname === H && (tt.setStep(1),
                            Z.goToRoute("/"),
                            Te.setIsUnlockAccount(!0))),
                            l.setItem("MOBILE_NUMBER", Te.mobileNumber);
                        else {
                            const e = this.getLoginSource();
                            $.sendEvent(V.LOGIN_FAILED, {
                                "User status": "REJECTED",
                                "Login Step": "1FA",
                                "Phone number": Te.mobileNumber,
                                "Login Failure Reason": `${i.error.message} [${i.error.code}]`,
                                "Login Failure Error Code": String(i.error.code),
                                "Profile ID": null === (r = null == Te ? void 0 : Te.userProfile) || void 0 === r ? void 0 : r.profileId,
                                ...e && {
                                    Source: e
                                }
                            }),
                            L.pushNotificationWithOverlay({
                                key: "1FA_OTP_GENERATE",
                                title: ke.generateErrorMessage(i.error.message, i.error.code),
                                type: "error",
                                code: i.error.code
                            })
                        }
                    }
                    ,
                    this.handleValidateOtpResponse = e=>{
                        var t, o;
                        "partner" === Te.application_type && e.redirectUri && Z.navigateOutside(e.redirectUri),
                        e.isSecretPinSet || null === (t = null === window || void 0 === window ? void 0 : window.dataLayer) || void 0 === t || t.push({
                            event: "Mobile_OTP_Submit"
                        }),
                        Te.setHasSecretPin(!Te.isUnlockAccount && e.isSecretPinSet),
                        Te.setUserId(null !== (o = e.userProfile.userId) && void 0 !== o ? o : ""),
                        Te.setUserProfile(e.userProfile),
                        Te.setUserType(e.userType),
                        Te.setProfileId(e.userProfile.profileId),
                        $.setUser(Te.profileId, Te.mobileNumber);
                        const r = {
                            domain: "upstox.com",
                            sameSite: "Strict"
                        };
                        m.setItem("profile_id", e.userProfile.profileId.toString(), r),
                        m.setItem("user_type", e.userType, r);
                        const i = this.getLoginSource();
                        $.sendEvent(V.LOGGED_IN, {
                            "User status": m.getItem("customer_status") || "NEW",
                            "Profile ID": e.userProfile.profileId,
                            "Login Step": "1FA",
                            "Phone number": Te.mobileNumber,
                            "User type": Te.userType,
                            ...i && {
                                Source: i
                            }
                        }),
                        Te.setPreviousStep(Te.step),
                        "LEAD" === e.userType ? this.checkLeadToken(!0) : Te.setStep(2)
                    }
                    ,
                    this.refreshAccessToken = async()=>{
                        (await Ue.request("REFRESH_ACCESS_TOKEN", "/refresh-access-token", "REFRESH_ACCESS_TOKEN", {
                            method: "POST",
                            query: this.getRefreshTokenParams()
                        }, !0)).success ? this.startOauth() : (Te.reset(),
                        X.push("/"))
                    }
                    ,
                    this.startOauth = async()=>{
                        const e = await Ue.request("AUTH", "/authorize", "OAUTH", {
                            method: "POST",
                            query: this.getOauthParams(),
                            body: {
                                data: {
                                    userOAuthApproval: !0
                                }
                            }
                        }, !0);
                        if (e.success) {
                            const {isApproved: t, redirectUri: o} = e.data;
                            t && o ? this.handleRedirect(o) : L.pushNotificationWithOverlay({
                                key: "OAUTH",
                                title: "Something went wrong",
                                type: "error"
                            })
                        } else
                            4000001 === e.error.code ? this.refreshAccessToken() : L.pushNotificationWithOverlay({
                                key: "OAUTH",
                                title: ke.generateErrorMessage(e.error.message, e.error.code),
                                type: "error",
                                code: e.error.code
                            })
                    }
                    ,
                    this.checkLeadToken = async(e=!1)=>{
                        var t, o;
                        const r = await Ue.request("LEAD_LOGIN", "/leads/2fa", "1FA_OTP", {
                            method: "POST",
                            headers: Te.getPinRequestHeaders,
                            query: Te.pinRequestsQuery
                        }, e);
                        if ((null == r ? void 0 : r.success) && (null == r ? void 0 : r.data)) {
                            const {userType: e, redirectUri: t, isSecretPinRequired: o, isSecretPinSet: i} = r.data
                              , n = i && o;
                            Te.setUserType(e),
                            m.setItem("user_type", e, {
                                domain: "upstox.com",
                                sameSite: "Strict"
                            }),
                            Te.setHasSecretPin(i),
                            "LEAD" !== e || n ? Te.setStep(2) : this.handleRedirect(t, !0)
                        } else
                            L.pushNotificationWithOverlay({
                                key: "CHECK_LEAD_TOKEN",
                                title: ke.generateErrorMessage((null === (t = r.error) || void 0 === t ? void 0 : t.message) || "Something went wrong. Please try again after some time.", (null === (o = r.error) || void 0 === o ? void 0 : o.code) || 1e6),
                                type: "error"
                            })
                    }
                    ,
                    this.handleRedirect = (e,t=!1)=>{
                        let o = `${e}${Te.redirectPath}`;
                        Te.devRedirectUri && (o = `${Te.devRedirectUri}${Te.redirectPath}`),
                        Te.workflow && Te.workflowVersion && (o += `?workflow=${Te.workflow}&workflow_version=${Te.workflowVersion}`),
                        Te.redirectQuery && (o += `?${Te.redirectQuery}`),
                        t && (Te.setHasSecretPin(!0),
                        Te.setIsRedirecting(!0)),
                        e !== Z.getExternalLinkByKey("WEBINAR_APP") ? Te.isLead ? this.handleProWebCustomerRedirect("UPSTOX_APP") : !Te.devRedirectUri && Te.isProWeb4App ? this.handleProWebCustomerRedirect("OLD_PRO_APP") : Z.navigateOutside(o) : this.handleWebinarCustomRedirect("WEBINAR_APP")
                    }
                    ,
                    this.handleWebinarCustomRedirect = e=>{
                        var t;
                        let o = Z.getExternalLinkByKey(e);
                        const {webinar_landing_page: r, webinar_id: i} = (0,
                        W.parse)(null === (t = null === window || void 0 === window ? void 0 : window.location) || void 0 === t ? void 0 : t.search) || {};
                        r && (o += `/${r}?webinar_id=${i}`),
                        Z.navigateOutside(o)
                    }
                    ,
                    this.handleProWebCustomerRedirect = e=>{
                        let t = Z.getExternalLinkByKey(e);
                        Te.redirectQuery && (t += `?${Te.redirectQuery}`),
                        Z.navigateOutside(t)
                    }
                    ,
                    this.autoLoginRequest = async()=>{
                        const {userId: e, token: t} = this.parseAutoLoginParams()
                          , o = {
                            "X-User-Id": e || "",
                            "X-Client-Id": Te.clientId
                        }
                          , r = await Ue.request("AUTOLOGIN", "/submit", "AUTOLOGIN", {
                            method: "POST",
                            query: this.getOauthParams(),
                            headers: o,
                            body: {
                                data: {
                                    userId: e,
                                    autoLoginToken: t
                                }
                            }
                        });
                        r.success ? (Te.setUserId(e || ""),
                        this.handleRedirect(r.data.redirectUri)) : (Te.reset(),
                        Z.goToRoute("/"))
                    }
                    ,
                    this.autoLoginQRRequest = async e=>{
                        const {userId: t} = this.parseAutoLoginParams()
                          , o = {
                            "X-User-Id": t || "",
                            "X-Client-Id": Te.clientId
                        }
                          , r = await Ue.request("AUTOLOGINQR", "/auto-login/submit", "AUTOLOGINQR", {
                            method: "POST",
                            query: this.getOauthParams(),
                            headers: o,
                            body: {
                                data: {
                                    userId: t,
                                    autoLoginToken: e
                                }
                            }
                        });
                        r.success ? (Te.setUserId(t || ""),
                        this.handleRedirect(r.data.redirectUri)) : (Te.reset(),
                        Z.goToRoute("/"))
                    }
                    ,
                    this.getLoginSource = ()=>"PW3" === Te.platformId ? U.WEB : "UTV" === Te.platformId ? U.TV : null,
                    this.remoteConfig = async()=>{
                        var e, t;
                        try {
                            const o = "post-trade/login-config.json"
                              , r = await Ue.request("AWS_UPSTOX", "/platform/web", "REMOTE_CONFIG", {
                                pathParameter: o,
                                query: {
                                    v: Date.now()
                                },
                                overrideCredentials: "same-origin",
                                headers: {
                                    "Content-Type": "text/plain"
                                },
                                overrideHeaders: !0,
                                addRequestIdHeader: !1
                            });
                            (null === (e = null == r ? void 0 : r.qrLogin) || void 0 === e ? void 0 : e.enabled) ? Te.setQrConfig(r) : Te.setQrConfig({
                                qrLogin: {
                                    enabled: !1
                                }
                            }),
                            Te.setQrLoginEnabled(!!(null === (t = null == r ? void 0 : r.qrLogin) || void 0 === t ? void 0 : t.enabled))
                        } catch (e) {
                            Te.setQrConfig({
                                qrLogin: {
                                    enabled: !1
                                }
                            }),
                            Te.setQrLoginEnabled(!1)
                        }
                    }
                    ,
                    this.getRequestIdParam = ()=>({
                        requestId: `${Te.platformId}${ke.generateUniqueId()}`
                    }),
                    this.getOauthParams = ()=>({
                        ...this.getRequestIdParam(),
                        client_id: Te.clientId,
                        response_type: "code",
                        redirect_uri: Te.redirectUrl
                    }),
                    this.getRefreshTokenParams = ()=>({
                        client_id: Te.clientId,
                        response_type: "token",
                        redirect_uri: Te.redirectUrl
                    }),
                    this.parseAutoLoginParams = ()=>{
                        const e = new URL(window.location.href).searchParams;
                        return {
                            token: e.get("token"),
                            userId: e.get("user_id")
                        }
                    }
                    ,
                    this.handleAuthCookieChange = (e,t)=>{
                        "delete" === e && "profile_id" === t && (Te.reset(),
                        Z.goToRoute("/", {
                            query: {
                                redirect_uri: Te.redirectUrl,
                                client_id: Te.clientId,
                                platform_id: Te.platformId,
                                redirect_path: Te.redirectPath
                            }
                        }))
                    }
                    ,
                    this.checkMobileNumberCookie = ()=>!!m.getItem("lead_phone_number");
                    const e = Z.getQuery();
                    1 === Te.step && this.generateOtpRequest(),
                    Te.setLoginCredentials(e),
                    "partner" === e.application_type && "mobikwik-ipo" === e.utm_source && (b.setTheme("mobikwik"),
                    Te.setIsIPOApp(!0)),
                    m.subscribeCookieChange("profile_id", this.handleAuthCookieChange)
                }
            }
              , so = (0,
            n.Pi)((()=>r.createElement(R.View, {
                justifyContent: "center",
                alignItems: "flex-start",
                flex: !0
            }, r.createElement(to, null))))
              , ao = (0,
            n.Pi)((()=>((0,
            r.useEffect)((()=>{
                no.logout()
            }
            ), []),
            r.createElement("div", null, r.createElement(fr, null)))))
              , co = ()=>({
                flex: "3 1 auto"
            })
              , lo = (0,
            n.Pi)((()=>((0,
            r.useEffect)((()=>{
                no.autoLoginRequest()
            }
            ), []),
            r.createElement(R.View, {
                css: co,
                justifyContent: "center",
                alignItems: "center"
            }, r.createElement(fr, null)))))
              , uo = ()=>r.createElement(R.View, {
                justifyContent: "center",
                alignItems: "flex-start",
                flex: !0
            }, r.createElement(io, null));
            var po = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class mo extends pe {
                constructor() {
                    super(...arguments),
                    this.deactivationReason = null,
                    this.deactivationCriterias = [],
                    this.otpData = null,
                    this.otp = "",
                    this.otpError = "",
                    this.setDeactivationReason = e=>{
                        this.deactivationReason = e
                    }
                    ,
                    this.setDeactivationsCriterias = e=>{
                        this.deactivationCriterias = e
                    }
                    ,
                    this.setOTPData = e=>{
                        const {message: t, nextRequestInterval: o, sessionToken: r} = e;
                        this.otpData = {
                            message: t,
                            nextRequestInterval: 1e3 * o,
                            sessionToken: r
                        }
                    }
                    ,
                    this.setOTP = e=>{
                        this.otp = e
                    }
                    ,
                    this.setOTPError = e=>{
                        this.otpError = e
                    }
                    ,
                    this.goBackFromReasonForm = ()=>{
                        this.step -= 1,
                        this.deactivationReason = ""
                    }
                }
            }
            po([s.observable], mo.prototype, "deactivationReason", void 0),
            po([s.observable], mo.prototype, "deactivationCriterias", void 0),
            po([s.observable], mo.prototype, "otpData", void 0),
            po([s.observable], mo.prototype, "otp", void 0),
            po([s.observable], mo.prototype, "otpError", void 0),
            po([s.action], mo.prototype, "setDeactivationReason", void 0),
            po([s.action], mo.prototype, "setDeactivationsCriterias", void 0),
            po([s.action], mo.prototype, "setOTPData", void 0),
            po([s.action], mo.prototype, "setOTP", void 0),
            po([s.action], mo.prototype, "setOTPError", void 0),
            po([s.action], mo.prototype, "goBackFromReasonForm", void 0);
            const ho = new mo
              , go = new class {
                constructor() {
                    this.validateDeactivationAccountPossibility = async()=>{
                        const e = await Ue.request("DEACTIVATION", "/validate-deactivate-account", "DEACTIVATION_VALIDATE", {
                            method: "GET",
                            query: {
                                entryPointCheck: !1
                            }
                        });
                        e.success && (ho.setDeactivationsCriterias(e.data.validationResults),
                        ho.setStep(3)),
                        e.error && L.pushNotificationWithOverlay({
                            key: "DEACTIVATION_VALIDATE",
                            title: e.error.message,
                            type: "error"
                        })
                    }
                    ,
                    this.generateOTP = async e=>{
                        const t = await Ue.request("DEACTIVATION", "/generate-otp", "DEACTIVATION_GENERATE_OTP", {
                            method: "POST",
                            body: {
                                data: {
                                    purpose: "ACCOUNT_DEACTIVATION",
                                    deactivationReason: ho.deactivationReason
                                }
                            }
                        });
                        t.success && (ho.setOTPData(t.data),
                        e || ho.setStep(5),
                        L.pushNotificationWithOverlay({
                            key: "DEACTIVATION_GENERATE_OTP",
                            title: t.data.message,
                            type: "success"
                        })),
                        t.error && L.pushNotificationWithOverlay({
                            key: "DEACTIVATION_GENERATE_OTP",
                            title: t.error.message,
                            type: "error"
                        })
                    }
                    ,
                    this.verifyOTP = async e=>{
                        var t;
                        const o = await Ue.request("DEACTIVATION", "/verify-otp", "DEACTIVATION_VERIFY_OTP", {
                            method: "POST",
                            body: {
                                data: e
                            }
                        });
                        o.success && ($.sendEvent(V.ACCOUNT_DEACTIVATED, {
                            "Profile ID": String(null === (t = Te.userProfile) || void 0 === t ? void 0 : t.profileId),
                            "Account deactivation reason": ho.deactivationReason,
                            "Account Status": "Deactivated",
                            "Last date of reactivation": String(Date.now())
                        }),
                        ho.setStep(6)),
                        o.error && ho.setOTPError(o.error.message)
                    }
                }
            }
              , fo = o.p + "assets/grow.svg"
              , vo = o.p + "assets/diagram.svg"
              , Eo = ({theme: e, cssProps: {isMobile: t}})=>({
                background: (0,
                R.color)(e, "background.default"),
                width: "100%",
                height: "100%",
                ...!t && {
                    maxWidth: 448,
                    minWidth: 320,
                    borderRadius: 8
                }
            })
              , yo = (0,
            n.Pi)((({title: e, subtitle: t, rightElement: o, children: i})=>{
                const {step: n, goStepBack: s, goBackFromReasonForm: a} = A("DeactivateAccountStore")
                  , {isMobile: c} = A("PlatformStore")
                  , l = (0,
                r.useMemo)((()=>{
                    const e = [0, 20, 20];
                    return {
                        title: c ? e : [0, 48, 20],
                        content: c ? e : [0, 48, 48]
                    }
                }
                ), [c]);
                return r.createElement(R.View, {
                    justifyContent: "flex-start",
                    flexDirection: "column",
                    css: Eo,
                    cssProps: {
                        isMobile: c
                    }
                }, r.createElement(R.View, {
                    justifyContent: n ? "space-between" : "flex-end",
                    padding: 20,
                    inline: !0
                }, 0 !== n && r.createElement(R.ArrowLeftIcon, {
                    cursor: "pointer",
                    onClick: 2 === n ? a : s,
                    size: "large"
                }), o || r.createElement(R.SupportCircleIcon, {
                    onClick: ()=>{
                        Z.openInNewTab("https://help.upstox.com/support/home")
                    }
                    ,
                    cursor: "pointer",
                    size: "large",
                    color: "text.2"
                })), r.createElement(R.View, {
                    flexDirection: "column",
                    gap: 8,
                    padding: l.title
                }, e, t), r.createElement(R.View, {
                    flex: !0,
                    padding: l.content
                }, i))
            }
            ))
              , bo = (0,
            n.Pi)((()=>{
                const {setStep: e} = A("DeactivateAccountStore");
                return r.createElement(yo, {
                    title: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "heading2"
                    }, "Are you sure you want to close your account?"),
                    subtitle: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "body"
                    }, "Having an account with Upstox, gives you:")
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    justifyContent: "space-between"
                }, r.createElement(R.View, {
                    flexDirection: "column",
                    gap: "medium",
                    margin: ["large", 0]
                }, r.createElement(R.View, {
                    gap: "medium",
                    alignItems: "center"
                }, r.createElement("img", {
                    src: fo,
                    alt: "grow img"
                }), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.1",
                    size: "m"
                }, "Endless opportunities to grow your money.")), r.createElement(R.View, {
                    gap: "medium",
                    alignItems: "center"
                }, r.createElement("img", {
                    src: vo,
                    alt: "diagram img"
                }), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.1",
                    size: "m"
                }, "Easy-to-use platform to buy stocks, mutual funds, IPOs, and more."))), r.createElement(R.View, {
                    flexDirection: "column",
                    gap: "small",
                    margin: ["xlarge", 0, 0]
                }, r.createElement(R.Button, {
                    size: "large",
                    variant: "primary"
                }, "Keep my Upstox account"), r.createElement(R.Button, {
                    size: "large",
                    variant: "secondary",
                    onClick: ()=>e(1)
                }, "Close account"))))
            }
            ))
              , To = o.p + "assets/wallet.svg"
              , Po = o.p + "assets/timer.svg"
              , wo = (0,
            n.Pi)((()=>{
                const {setStep: e} = A("DeactivateAccountStore");
                return r.createElement(yo, {
                    title: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "heading2"
                    }, "Deactivate your account instead of closing it."),
                    subtitle: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "body"
                    }, "If you just want to take a temporary break from trading, we recommend to deactivate your account. By doing so, you’ll be able to:")
                }, r.createElement(R.View, {
                    flexDirection: "column"
                }, r.createElement(R.View, {
                    flexDirection: "column",
                    gap: "medium",
                    margin: ["large", 0]
                }, r.createElement(R.View, {
                    gap: "medium",
                    alignItems: "center"
                }, r.createElement("img", {
                    src: To,
                    alt: "grow img"
                }), r.createElement(R.View, {
                    flexDirection: "column",
                    gap: "xxsmall"
                }, r.createElement(R.Text, {
                    variant: "heading3",
                    color: "text.1"
                }, "Maintain your account at zero charges"), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.2",
                    size: "s",
                    lineHeight: "s"
                }, "You can keep your account deactivated for up to one year, free of charge."))), r.createElement(R.View, {
                    gap: "medium",
                    alignItems: "center"
                }, r.createElement("img", {
                    src: Po,
                    alt: "diagram img"
                }), r.createElement(R.View, {
                    flexDirection: "column",
                    gap: "xxsmall"
                }, r.createElement(R.Text, {
                    variant: "heading3",
                    color: "text.1"
                }, "Resume trading, instantly"), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.2",
                    size: "s",
                    lineHeight: "s"
                }, "No account opening fee. No need to redo the account opening process.")))), r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    gap: "small",
                    margin: ["large", 0]
                }, r.createElement(R.Button, {
                    size: "large",
                    variant: "primary",
                    onClick: ()=>e(2)
                }, "Deactivate account")), r.createElement(R.Divider, null), r.createElement(R.View, {
                    flexDirection: "column",
                    gap: "small",
                    margin: ["medium", 0, "xxsmall"]
                }, r.createElement(R.WarningIcon, {
                    size: "large",
                    color: "data.negative"
                }), r.createElement(R.Text, {
                    variant: "bodyBold",
                    color: "text.1",
                    size: "m"
                }, "Close account permanently"), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.1",
                    size: "m"
                }, "To reopen your account, you’ll have to go through the KYC process again. You’ll get a fresh demat account and might have to pay the account opening charges."), r.createElement(R.View, {
                    flexDirection: "column",
                    margin: ["medium", 0, 0]
                }, r.createElement(R.Button, {
                    size: "large",
                    variant: "secondary"
                }, "Continue to close account")))))
            }
            ))
              , Io = 12e4
              , xo = {
                takingABreak: "Taking a break from trading",
                insufficientFunds: "Insufficient funds for trading",
                monthlyCharges: "Don’t want to pay monthly account maintenance charges",
                otherProduct: "Moved to some other product",
                unsatisfiedWithSupport: "Unsatisfied with customer support"
            }
              , Oo = {
                NON_NEGATIVE_LIMIT_BALANCE: `${{
                    PROD: "https://app.upstox.com",
                    UAT: "https://uat-pro-4.upstox.com",
                    QA: "https://app.upstox.com"
                }[P]}/user/wallets`,
                PENDING_HOLDINGS: "https://help.upstox.com/a/solutions/articles/252219",
                OPEN_ORDERS: "https://help.upstox.com/a/solutions/articles/252220",
                ONGOING_SIP: "https://upstox.com/mutual-funds/portfolio",
                RECENTLY_REACTIVATED: "https://help.upstox.com/a/solutions/articles/252217",
                DORMANT_ACCOUNT: "https://help.upstox.com/a/solutions/articles/252218"
            }
              , So = ({theme: e})=>({
                display: "grid",
                width: "100%",
                flexDirection: "row",
                gridTemplateColumns: "25px 1fr",
                gridColumnGap: (0,
                R.spacing)(e, "medium"),
                cursor: "pointer"
            })
              , Ao = (0,
            n.Pi)((()=>{
                const {setDeactivationReason: e, deactivationReason: t} = A("DeactivateAccountStore")
                  , {loadings: {DEACTIVATION_VALIDATE: o}} = A("LoadingStore")
                  , i = (0,
                r.useMemo)((()=>Boolean(t && !Object.values(xo).includes(t))), [t]);
                return r.createElement(yo, {
                    title: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "heading2"
                    }, "We’re sorry to see you go"),
                    subtitle: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "body"
                    }, "Your feedback matters. Tell us why you’re deactivating your account.")
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    justifyContent: "space-between",
                    gap: "large"
                }, r.createElement(R.View, {
                    as: "form",
                    name: "reason",
                    id: "deactivation-reason-form",
                    flex: !0,
                    flexDirection: "column",
                    gap: "large",
                    css: ()=>({
                        width: "100%"
                    }),
                    onSubmit: e=>{
                        e.preventDefault(),
                        go.validateDeactivationAccountPossibility()
                    }
                }, r.createElement(R.View, {
                    margin: ["medium", 0, 0],
                    alignItems: "center",
                    onClick: ()=>e(xo.takingABreak),
                    css: So
                }, r.createElement(R.Radio, {
                    readOnly: !0,
                    checked: t === xo.takingABreak,
                    name: "takingABreak"
                }), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.1"
                }, xo.takingABreak)), r.createElement(R.View, {
                    alignItems: "center",
                    onClick: ()=>e(xo.insufficientFunds),
                    css: So
                }, r.createElement(R.Radio, {
                    readOnly: !0,
                    checked: t === xo.insufficientFunds,
                    name: "insufficientFunds"
                }), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.1"
                }, xo.insufficientFunds)), r.createElement(R.View, {
                    alignItems: "center",
                    onClick: ()=>e(xo.monthlyCharges),
                    css: So
                }, r.createElement(R.Radio, {
                    readOnly: !0,
                    checked: t === xo.monthlyCharges,
                    name: "monthlyCharges"
                }), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.1"
                }, xo.monthlyCharges)), r.createElement(R.View, {
                    alignItems: "center",
                    onClick: ()=>e(xo.otherProduct),
                    css: So
                }, r.createElement(R.Radio, {
                    readOnly: !0,
                    checked: t === xo.otherProduct,
                    name: "otherProduct"
                }), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.1"
                }, xo.otherProduct)), r.createElement(R.View, {
                    alignItems: "center",
                    onClick: ()=>e(xo.unsatisfiedWithSupport),
                    css: So
                }, r.createElement(R.Radio, {
                    readOnly: !0,
                    checked: t === xo.unsatisfiedWithSupport,
                    name: "unsatisfiedWithSupport"
                }), r.createElement(R.Text, {
                    variant: "body",
                    color: "text.1"
                }, xo.unsatisfiedWithSupport)), r.createElement(R.View, {
                    alignItems: "center",
                    css: So
                }, r.createElement(R.Radio, {
                    checked: i,
                    name: "first"
                }), r.createElement(R.Input, {
                    name: "otherReason",
                    flex: !0,
                    type: "text",
                    variant: "secondary",
                    placeholder: "Other reason",
                    onChange: ({target: {value: t}})=>{
                        e(t)
                    }
                }))), r.createElement(R.Button, {
                    form: "deactivation-reason-form",
                    size: "large",
                    type: "submit",
                    variant: "primary",
                    disabled: !t,
                    isLoading: o
                }, "Continue")))
            }
            ))
              , Ro = ()=>({
                width: "100%",
                height: "360px"
            })
              , Co = ()=>({
                maxHeight: "100%",
                overflowY: "auto",
                overflowX: "hidden"
            })
              , ko = ({theme: e})=>({
                display: "grid",
                width: "90%",
                flexDirection: "row",
                gridTemplateColumns: "56px 1fr",
                gridColumnGap: (0,
                R.spacing)(e, "medium")
            })
              , _o = (0,
            n.Pi)((()=>{
                const {setStep: e, deactivationCriterias: t} = A("DeactivateAccountStore");
                return r.createElement(yo, {
                    title: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "heading2"
                    }, "To deactivate your account, you need to:")
                }, r.createElement(R.View, {
                    flexDirection: "column",
                    justifyContent: "space-between",
                    css: Ro
                }, r.createElement(R.View, {
                    flexDirection: "column",
                    css: Co,
                    gap: "large",
                    margin: ["xlarge", 0, 0]
                }, t.map((e=>r.createElement(R.View, {
                    key: e.code,
                    alignItems: "center",
                    css: ko
                }, r.createElement(R.ContainedIcon, null, r.createElement(R.CheckboxCheckedIcon, {
                    size: "large",
                    color: e.validationStatus ? "background.green" : "background.tan"
                })), r.createElement(R.View, {
                    flexDirection: "column",
                    alignItems: "flex-start"
                }, r.createElement(R.Text, {
                    variant: "heading3",
                    color: "text.1"
                }, e.message), r.createElement(R.Text, {
                    as: "button",
                    onClick: ()=>{
                        return t = e.code,
                        void Z.openInNewTab(Oo[t]);
                        var t
                    }
                    ,
                    variant: "meta",
                    color: e.validationStatus ? "disabled.3" : "text.link",
                    disabled: e.validationStatus
                }, "NON_NEGATIVE_LIMIT_BALANCE" === e.code ? "See wallet" : "Learn more")))))), t.every((e=>e.validationStatus)) && r.createElement(R.Button, {
                    size: "large",
                    variant: "primary",
                    onClick: ()=>e(4)
                }, "Continue to deactivate")))
            }
            ))
              , No = ()=>({
                width: "100%"
            })
              , Do = (0,
            n.Pi)((()=>{
                const {loadings: {DEACTIVATION_GENERATE_OTP: e}} = A("LoadingStore");
                return r.createElement(yo, {
                    title: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "heading2"
                    }, "Continue to deactivate account"),
                    subtitle: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "body"
                    }, "To ensure your account’s security, we’ll be sending a one-time password to your registered mobile number.")
                }, r.createElement(R.View, {
                    flexDirection: "column",
                    margin: ["large", 0, 0],
                    css: No
                }, r.createElement(R.Button, {
                    width: "full",
                    size: "large",
                    variant: "primary",
                    onClick: ()=>go.generateOTP(!1),
                    isLoading: e
                }, "Get OTP")))
            }
            ))
              , Lo = (0,
            n.Pi)((()=>{
                const {otpData: e, setOTP: t, otp: o, setOTPError: i, otpError: n} = A("DeactivateAccountStore")
                  , {loadings: {DEACTIVATION_VERIFY_OTP: s}} = A("LoadingStore")
                  , [a,c] = $e(Io)
                  , l = 0 === a;
                return r.createElement(yo, {
                    title: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "heading2"
                    }, "OTP sent"),
                    subtitle: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "body"
                    }, null == e ? void 0 : e.message),
                    rightElement: l ? r.createElement(R.Button, {
                        variant: "invisible",
                        size: "small",
                        onClick: ()=>{
                            go.generateOTP(!0),
                            c((null == e ? void 0 : e.nextRequestInterval) || Io)
                        }
                    }, "Send OTP again") : r.createElement(R.Text, {
                        variant: "metaBold",
                        size: "m"
                    }, `Please wait (${a / 1e3}s)`)
                }, r.createElement(R.View, {
                    as: "form",
                    flexDirection: "column",
                    id: "otp-form",
                    onSubmit: t=>{
                        t.preventDefault(),
                        go.verifyOTP({
                            otp: o,
                            sessionToken: null == e ? void 0 : e.sessionToken
                        })
                    }
                    ,
                    margin: ["large", 0, 0],
                    flex: !0
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    margin: [0, 0, "large", 0]
                }, r.createElement(R.View, {
                    inline: !1
                }, r.createElement(R.MaskedInput, {
                    as: R.InputField,
                    mask: [/\d/, /\d/, /\d/, "-", /\d/, /\d/, /\d/],
                    guide: !1,
                    disabled: s,
                    type: "text",
                    label: "Enter OTP",
                    value: o,
                    onChange: e=>{
                        n && i(""),
                        t(e.target.value.replace("-", ""))
                    }
                    ,
                    error: n,
                    variant: "secondary",
                    flex: !0
                }))), r.createElement(R.View, {
                    margin: ["xlarge", 0, 0]
                }, r.createElement(R.Button, {
                    width: "full",
                    variant: "primary",
                    type: "submit",
                    isLoading: s,
                    disabled: 6 !== (null == o ? void 0 : o.length)
                }, "Continue"))))
            }
            ))
              , Vo = ({theme: e, cssProps: {isDesktop: t}})=>({
                background: (0,
                R.color)(e, "background.default"),
                width: 448,
                borderRadius: 8,
                ...!t && {
                    width: "100%",
                    height: "100%",
                    borderRadius: 0
                }
            })
              , Uo = ({theme: e})=>({
                color: (0,
                R.color)(e, "background.green"),
                width: 42,
                height: 42
            })
              , qo = {
                0: bo,
                1: wo,
                2: Ao,
                3: _o,
                4: Do,
                5: Lo,
                6: (0,
                n.Pi)((()=>{
                    const {isMobile: e} = A("PlatformStore");
                    return r.createElement(R.View, {
                        flex: !0,
                        flexDirection: "column",
                        css: Vo,
                        cssProps: {
                            isDesktop: !e
                        },
                        padding: e ? [0, 20, 20] : [48]
                    }, r.createElement(R.View, {
                        flexDirection: "column",
                        gap: "large",
                        margin: ["medium", "medium", "xxlarge"]
                    }, r.createElement(R.CheckboxCheckedIcon, {
                        size: "large",
                        color: "background.green",
                        css: Uo
                    }), r.createElement(R.Text, {
                        color: "text.1",
                        variant: "heading2"
                    }, "Your account has been deactivated"), r.createElement(R.Text, {
                        color: "text.1",
                        variant: "body"
                    }, "To reactivate, log in to your account using the same credentials that you use now.")), r.createElement(R.View, {
                        flexDirection: "column",
                        padding: ["xxlarge", "medium", "medium"]
                    }, r.createElement(R.View, {
                        flexDirection: "column",
                        gap: "small"
                    }, r.createElement(R.Text, {
                        variant: "metaBold",
                        color: "text.1"
                    }, "Last date for reactivating your account"), r.createElement(R.View, {
                        flexDirection: "column"
                    }, r.createElement(R.Text, {
                        variant: "metaBold",
                        color: "text.1"
                    }, "26. June. 2022"), r.createElement(R.Text, {
                        variant: "body",
                        color: "text.2",
                        size: "s"
                    }, "This date is calculated on the basis of your last trading activity. As per the government rule, an account has to be marked dormant if there’s no trading activity observed for a period of 12 months.")), r.createElement(R.View, {
                        flexDirection: "column",
                        gap: "xxsmall",
                        padding: ["medium", 0, 0]
                    }, r.createElement(R.Text, {
                        variant: "metaBold",
                        color: "text.1"
                    }, "Account reactivation charges"), r.createElement(R.Text, {
                        variant: "body",
                        color: "text.2",
                        size: "s"
                    }, "Rs. 0")), r.createElement(R.View, {
                        flexDirection: "column",
                        padding: ["small", 0, 0, 0]
                    }, r.createElement(R.Link, {
                        href: "/"
                    }, "Reactivate account")))))
                }
                ))
            }
              , Fo = ({cssProps: e})=>({
                ...e
            })
              , Mo = (0,
            n.Pi)((()=>{
                const {step: e} = A("DeactivateAccountStore")
                  , {isMobile: t} = A("PlatformStore")
                  , o = (0,
                r.useMemo)((()=>{
                    const t = qo[e];
                    return r.createElement(t, null)
                }
                ), [e]);
                return r.createElement(R.View, {
                    flex: !0,
                    alignItems: "center",
                    justifyContent: "center",
                    css: Fo,
                    cssProps: t ? {
                        width: "100%",
                        height: "100%"
                    } : void 0
                }, o)
            }
            ))
              , Bo = (0,
            n.Pi)((()=>r.createElement(R.View, {
                flex: !0,
                alignItems: "flex-start",
                justifyContent: "center"
            }, r.createElement(Mo, null))));
            var Wo = function(e, t, o, r) {
                var i, n = arguments.length, s = n < 3 ? t : null === r ? r = Object.getOwnPropertyDescriptor(t, o) : r;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    s = Reflect.decorate(e, t, o, r);
                else
                    for (var a = e.length - 1; a >= 0; a--)
                        (i = e[a]) && (s = (n < 3 ? i(s) : n > 3 ? i(t, o, s) : i(t, o)) || s);
                return n > 3 && s && Object.defineProperty(t, o, s),
                s
            };
            class jo extends pe {
                constructor() {
                    super(...arguments),
                    this.pan = "",
                    this.panError = "",
                    this.reactivationDueDate = "",
                    this.setPan = e=>{
                        this.pan = e
                    }
                    ,
                    this.setPanError = e=>{
                        this.panError = e
                    }
                    ,
                    this.setReactivationDueDate = e=>{
                        this.reactivationDueDate = e
                    }
                }
            }
            Wo([s.observable], jo.prototype, "pan", void 0),
            Wo([s.observable], jo.prototype, "panError", void 0),
            Wo([s.observable], jo.prototype, "reactivationDueDate", void 0),
            Wo([s.action], jo.prototype, "setPan", void 0),
            Wo([s.action], jo.prototype, "setPanError", void 0),
            Wo([s.action], jo.prototype, "setReactivationDueDate", void 0);
            const Qo = new jo
              , Go = new class {
                constructor() {
                    this.reactivateAccount = async()=>{
                        var e;
                        const t = await Ue.request("REACTIVATION", "/reactivate-account", "REACTIVATE_ACCOUNT", {
                            method: "POST",
                            body: {
                                data: {
                                    panNumber: Qo.pan
                                }
                            }
                        });
                        t.success && (Qo.setStep(1),
                        $.sendEvent(V.ACCOUNT_REACTIVATED, {
                            "Profile ID": String(null === (e = Te.userProfile) || void 0 === e ? void 0 : e.profileId),
                            "Account Status": "Deactivated"
                        }),
                        L.pushNotificationWithOverlay({
                            key: "REACTIVATION",
                            title: t.data.message,
                            type: "success"
                        })),
                        t.error && (Qo.setPanError(t.error.message),
                        L.pushNotificationWithOverlay({
                            key: "REACTIVATION",
                            title: t.error.message,
                            type: "error"
                        }))
                    }
                    ,
                    this.getReactivationDetails = async()=>{
                        const e = await Ue.request("REACTIVATION", "/reactivation-details", "REACTIVATION_DETAILS", {
                            method: "GET"
                        });
                        if (e.success) {
                            const t = ke.formatDate(e.data.reactivationDueDate, "DD.MM.YYYY");
                            Qo.setReactivationDueDate(t)
                        }
                        e.error && L.pushNotificationWithOverlay({
                            key: "REACTIVATION_DETAILS",
                            title: e.error.message,
                            type: "error"
                        })
                    }
                }
            }
              , zo = ({theme: e, cssProps: {isMobile: t}})=>({
                background: (0,
                R.color)(e, "background.default"),
                width: "100%",
                height: "100%",
                ...!t && {
                    maxWidth: 448,
                    minWidth: 320,
                    borderRadius: 8
                }
            })
              , $o = (0,
            n.Pi)((({title: e, subtitle: t, rightElement: o, children: i})=>{
                const {step: n, goStepBack: s} = A("ReactivateAccountStore")
                  , {isMobile: a} = A("PlatformStore")
                  , c = (0,
                r.useMemo)((()=>{
                    const e = [0, 20, 20];
                    return {
                        title: a ? e : [0, 48, 20],
                        content: a ? e : [0, 48, 48]
                    }
                }
                ), [a]);
                return r.createElement(R.View, {
                    justifyContent: "flex-start",
                    flexDirection: "column",
                    css: zo,
                    cssProps: {
                        isMobile: a
                    }
                }, r.createElement(R.View, {
                    justifyContent: n ? "space-between" : "flex-end",
                    padding: 16,
                    inline: !0
                }, 0 !== n && r.createElement(R.ArrowLeftIcon, {
                    cursor: "pointer",
                    onClick: s,
                    size: "large"
                }), o || r.createElement(R.SupportCircleIcon, {
                    cursor: "pointer",
                    size: "large",
                    color: "text.2"
                })), r.createElement(R.View, {
                    flexDirection: "column",
                    gap: 8,
                    padding: c.title
                }, e, t), r.createElement(R.View, {
                    flex: !0,
                    padding: c.content
                }, i))
            }
            ))
              , Ho = (0,
            n.Pi)((()=>{
                const {pan: e, setPan: t, panError: o, setPanError: i, reactivationDueDate: n} = A("ReactivateAccountStore")
                  , {loadings: {REACTIVATE_ACCOUNT: s}} = A("LoadingStore");
                return r.createElement($o, {
                    title: r.createElement(R.Text, {
                        color: "text.1",
                        variant: "heading2"
                    }, "Reactivate your account"),
                    subtitle: r.createElement(R.Text, {
                        variant: "body",
                        color: "text.2"
                    }, "You can reactivate your Upstox account by verifying your PAN card details.")
                }, r.createElement(R.View, {
                    as: "form",
                    flexDirection: "column",
                    id: "pan-form",
                    onSubmit: t=>{
                        t.preventDefault(),
                        (Ye.isPANCard(e) ? (i(""),
                        1) : (i("Please check your PAN number and try again."),
                        0)) && Go.reactivateAccount()
                    }
                    ,
                    flex: !0
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    justifyContent: "space-between"
                }, r.createElement(R.View, {
                    flexDirection: "column"
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    padding: ["small", 0, "xlarge"]
                }, r.createElement(R.InputField, {
                    label: "Enter your PAN",
                    variant: "secondary",
                    value: e,
                    error: o,
                    onChange: ({target: {value: e}})=>{
                        t(e.toUpperCase()),
                        i("")
                    }
                    ,
                    InputProps: {
                        fixedLength: 10
                    }
                })), r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    justifyContent: "space-between",
                    gap: "medium"
                }, r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    gap: "xxsmall"
                }, r.createElement(R.Text, {
                    variant: "meta"
                }, "Last date for reactivating account"), r.createElement(R.Text, {
                    variant: "metaBold",
                    color: "text.1"
                }, n)), r.createElement(R.View, {
                    flex: !0,
                    flexDirection: "column",
                    gap: "xxsmall"
                }, r.createElement(R.Text, {
                    variant: "meta"
                }, "Reactivation Fees"), r.createElement(R.Text, {
                    variant: "metaBold",
                    color: "text.1"
                }, "Rs. 0")))), r.createElement(R.View, {
                    flexDirection: "column",
                    margin: ["large", 0, 0]
                }, r.createElement(R.Button, {
                    isLoading: s,
                    type: "submit"
                }, "Reactivate my account")))))
            }
            ))
              , Ko = ({theme: e, cssProps: {isMobile: t}})=>({
                background: (0,
                R.color)(e, "background.default"),
                width: "100%",
                height: "100%",
                ...!t && {
                    maxWidth: 448,
                    minWidth: 320,
                    borderRadius: 8
                }
            })
              , Yo = ({theme: e})=>({
                color: (0,
                R.color)(e, "background.green"),
                width: 66,
                height: 66
            })
              , Xo = {
                0: Ho,
                1: (0,
                n.Pi)((()=>{
                    const {isMobile: e} = A("PlatformStore");
                    return r.createElement(R.View, {
                        flexDirection: "column",
                        css: Ko,
                        cssProps: {
                            isMobile: e
                        }
                    }, r.createElement(R.View, {
                        flex: !0,
                        flexDirection: "column",
                        margin: e ? [20] : [48],
                        justifyContent: "space-between"
                    }, r.createElement(R.View, null, r.createElement(R.View, {
                        flexDirection: "column",
                        gap: "large"
                    }, r.createElement(R.CheckboxCheckedIcon, {
                        size: "large",
                        color: "background.green",
                        css: Yo
                    }), r.createElement(R.Text, {
                        color: "text.1",
                        variant: "heading1"
                    }, "Congratulations! Your account is reactivated."), r.createElement(R.Text, {
                        color: "text.2",
                        variant: "body"
                    }, "Your Upstox account is ready to start trading and investing."))), r.createElement(R.View, {
                        flexDirection: "column",
                        margin: ["xlarge", 0, 0]
                    }, r.createElement(R.Button, {
                        onClick: no.logout,
                        size: "large"
                    }, "Re Login"))))
                }
                ))
            }
              , Jo = ({cssProps: e})=>({
                ...e
            })
              , Zo = (0,
            n.Pi)((()=>{
                const {step: e} = A("ReactivateAccountStore")
                  , {isMobile: t} = A("PlatformStore")
                  , {loadings: {REACTIVATION_DETAILS: o}} = A("LoadingStore");
                (0,
                r.useEffect)((()=>{
                    Go.getReactivationDetails()
                }
                ), []);
                const i = (0,
                r.useMemo)((()=>{
                    const t = Xo[e];
                    return r.createElement(t, null)
                }
                ), [e]);
                return o ? r.createElement(fr, null) : r.createElement(R.View, {
                    css: Jo,
                    cssProps: t ? {
                        width: "100%",
                        height: "100%"
                    } : void 0
                }, i)
            }
            ))
              , er = (0,
            n.Pi)((()=>r.createElement(R.View, {
                flex: !0,
                alignItems: "flex-start",
                justifyContent: "center"
            }, r.createElement(Zo, null))))
              , tr = (0,
            n.Pi)((()=>{
                const {isLead: e} = A("AuthStore");
                return r.createElement(Et, {
                    stepControllerStoreKey: "ForgotPinStore",
                    title: r.createElement(R.Text, {
                        variant: "heading2",
                        color: "text.1"
                    }, "Unlock account"),
                    subtitle: r.createElement(R.Text, {
                        variant: "body",
                        color: "text.2"
                    }, e ? "To set a new PIN, you’ll get a one-time password (OTP) on your mobile number." : "To keep your account secure, we need to verify it’s you.")
                }, e ? r.createElement(It, {
                    storeKey: "ForgotPinStore"
                }) : r.createElement(ro, null))
            }
            ))
              , or = ()=>r.createElement(R.View, {
                justifyContent: "center",
                alignItems: "flex-start",
                flex: !0
            }, r.createElement(tr, null))
              , rr = (0,
            r.memo)((()=>r.createElement(le.SV, {
                fallbackRender: ()=>r.createElement(fr, null),
                onError: Z.errorHandler
            }, r.createElement(Tt, null, r.createElement(mr, null, r.createElement(S.rs, null, r.createElement(S.AW, {
                exact: !0,
                path: "/",
                component: so
            }), r.createElement(S.AW, {
                exact: !0,
                path: "/forgot-pin",
                component: uo
            }), r.createElement(S.AW, {
                exact: !0,
                path: H,
                component: or
            }), r.createElement(S.AW, {
                exact: !0,
                path: "/logout",
                component: ao
            }), r.createElement(S.AW, {
                exact: !0,
                path: "/auto-login",
                component: lo
            }), !O.isProduction && r.createElement(S.AW, {
                path: "/deactivate-account",
                component: Bo
            }), !O.isProduction && r.createElement(S.AW, {
                path: "/reactivate-account",
                component: er
            }), r.createElement(S.l_, {
                to: "/"
            })))))))
              , ir = (0,
            r.memo)((()=>r.createElement(ee, null, r.createElement(rr, null))))
              , nr = ()=>r.createElement(Pt, null)
              , sr = ({cssProps: {isMobile: e}})=>({
                ...!e && {
                    maxWidth: 340
                }
            })
              , ar = ()=>r.createElement(R.View, {
                css: sr
            }, r.createElement(R.Text, {
                variant: "meta",
                align: "center"
            }, "RKSV Securities India Pvt. Ltd: SEBI Regn No. INZ000185137 | NSE TM Code: 13942 | BSE TM Code: 6155 | CDSL: IN-DP-118-2015 | RKSV Commodities India Pvt. Ltd.: SEBI Regn. No. INZ000015837 | MCX TM Code: 46510"))
              , cr = ()=>({
                margin: "28px auto"
            })
              , lr = ({theme: e, cssProps: {isMobile: t}})=>({
                ...t && {
                    background: (0,
                    R.color)(e, "white"),
                    width: "100%"
                }
            })
              , ur = ()=>({
                maxWidth: 184
            })
              , dr = ({theme: e})=>({
                width: "100vw",
                height: "100vh",
                overflow: "auto",
                background: (0,
                R.color)(e, "background.tan")
            })
              , pr = ()=>({
                width: "100%"
            })
              , mr = ({children: e})=>{
                const {isMobile: t} = A("PlatformStore")
                  , {isIPOApp: o, isTradingViewApp: i} = A("AuthStore")
                  , {pathname: n} = (0,
                S.TH)();
                return r.createElement(R.View, {
                    css: dr,
                    flexDirection: "column"
                }, !t && r.createElement(R.View, {
                    css: cr,
                    alignItems: "center"
                }, !o && r.createElement(r.Fragment, null, r.createElement("img", {
                    src: _,
                    alt: "upsxtox-logo"
                }), i && r.createElement(r.Fragment, null, r.createElement("img", {
                    src: k,
                    alt: "pipe img",
                    style: {
                        padding: "0px 16px"
                    }
                }), r.createElement("img", {
                    src: C,
                    alt: "trading-view logo"
                })))), r.createElement(R.View, {
                    flexDirection: "column",
                    alignItems: "stretch"
                }, r.createElement(ce, null)), e, "/" === n && r.createElement(r.Fragment, null, o && r.createElement(R.View, {
                    css: lr,
                    cssProps: {
                        isMobile: t
                    },
                    padding: [0, 0, 12],
                    justifyContent: "center"
                }, r.createElement(R.View, {
                    css: ur,
                    flex: !0,
                    alignItems: "center"
                }, r.createElement(R.Text, null, "Powered by"), r.createElement(R.View, {
                    padding: [0, 12]
                }, r.createElement("img", {
                    src: _,
                    alt: "upsxtox-logo"
                })))), r.createElement(R.View, {
                    css: pr,
                    padding: [t ? 20 : 48],
                    justifyContent: "center",
                    alignItems: "center"
                }, r.createElement(ar, null))), r.createElement(nr, null))
            }
              , hr = (0,
            n.Pi)((({children: e})=>{
                const {theme: t} = A("AppStore");
                return r.createElement(R.FelaProvider, null, r.createElement(R.HideCursorFocus, null), r.createElement(R.ThemeProvider, {
                    theme: t
                }, e))
            }
            ))
              , gr = ()=>({
                height: "100%"
            })
              , fr = ()=>r.createElement(R.View, {
                flex: !0,
                justifyContent: "center",
                alignItems: "center",
                css: gr
            }, r.createElement(R.Loading, null))
              , vr = window.document.getElementById("modalRoot")
              , Er = (0,
            r.memo)((e=>r.createElement(R.Modal, {
                zIndex: 9,
                container: vr,
                ...e
            })))
              , yr = {
                AppStore: b,
                LoadingStore: Oe,
                AuthStore: Te,
                ErrorStore: De,
                NotificationStore: L,
                ForgotPinStore: tt,
                OtpStore: Me,
                PlatformStore: ge,
                DeactivateAccountStore: ho,
                ReactivateAccountStore: Qo,
                SecretPinStore: nt,
                RoutingStore: X
            };
            var br = o(265);
            se()(br.Z, {
                insert: "head",
                singleton: !1
            }),
            br.Z.locals,
            console.info(`Upstox Login v1.98.1-SNAPSHOT(${P})`),
            O.init(),
            $.init(),
            (0,
            s.configure)({
                computedRequiresReaction: !0,
                enforceActions: "observed"
            }),
            (0,
            i.render)(r.createElement(n.zt, {
                ...yr
            }, r.createElement(hr, null, r.createElement(ir, null))), window.document.getElementById("root"))
        }
    }, o = {};
    function r(e) {
        var i = o[e];
        if (void 0 !== i)
            return i.exports;
        var n = o[e] = {
            id: e,
            loaded: !1,
            exports: {}
        };
        return t[e].call(n.exports, n, n.exports, r),
        n.loaded = !0,
        n.exports
    }
    r.m = t,
    r.amdO = {},
    e = [],
    r.O = (t,o,i,n)=>{
        if (!o) {
            var s = 1 / 0;
            for (u = 0; u < e.length; u++) {
                for (var [o,i,n] = e[u], a = !0, c = 0; c < o.length; c++)
                    (!1 & n || s >= n) && Object.keys(r.O).every((e=>r.O[e](o[c]))) ? o.splice(c--, 1) : (a = !1,
                    n < s && (s = n));
                if (a) {
                    e.splice(u--, 1);
                    var l = i();
                    void 0 !== l && (t = l)
                }
            }
            return t
        }
        n = n || 0;
        for (var u = e.length; u > 0 && e[u - 1][2] > n; u--)
            e[u] = e[u - 1];
        e[u] = [o, i, n]
    }
    ,
    r.n = e=>{
        var t = e && e.__esModule ? ()=>e.default : ()=>e;
        return r.d(t, {
            a: t
        }),
        t
    }
    ,
    r.d = (e,t)=>{
        for (var o in t)
            r.o(t, o) && !r.o(e, o) && Object.defineProperty(e, o, {
                enumerable: !0,
                get: t[o]
            })
    }
    ,
    r.g = function() {
        if ("object" == typeof globalThis)
            return globalThis;
        try {
            return this || new Function("return this")()
        } catch (e) {
            if ("object" == typeof window)
                return window
        }
    }(),
    r.o = (e,t)=>Object.prototype.hasOwnProperty.call(e, t),
    r.r = e=>{
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    r.nmd = e=>(e.paths = [],
    e.children || (e.children = []),
    e),
    r.p = "/",
    (()=>{
        var e = {
            152: 0
        };
        r.O.j = t=>0 === e[t];
        var t = (t,o)=>{
            var i, n, [s,a,c] = o, l = 0;
            if (s.some((t=>0 !== e[t]))) {
                for (i in a)
                    r.o(a, i) && (r.m[i] = a[i]);
                if (c)
                    var u = c(r)
            }
            for (t && t(o); l < s.length; l++)
                n = s[l],
                r.o(e, n) && e[n] && e[n][0](),
                e[n] = 0;
            return r.O(u)
        }
          , o = self.webpackChunkupstox_login_2_0 = self.webpackChunkupstox_login_2_0 || [];
        o.forEach(t.bind(null, 0)),
        o.push = t.bind(null, o.push.bind(o))
    }
    )(),
    r.nc = void 0;
    var i = r.O(void 0, [885, 483, 578, 6, 958, 248, 694, 871, 980, 576, 727, 672, 74, 418, 122, 365, 352, 292, 213, 460, 369, 172], (()=>r(33720)));
    i = r.O(i)
}
)();
